import csv
import logging
import time

from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString, MultiLineString, Point, Polygon


logger = logging.getLogger(__name__)


def save_lat_lng_to_point(lat, lng):
    #  save a point to django Point
    #  https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/#creating-a-point-object
    point = Point(lng, lat)
    return point


def save_arrays_to_polygon(array_of_arrays):
    #  save a polygon to django Polygon
    #  https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/#creating-a-polygon-object
    polygon = Polygon(array_of_arrays)
    return polygon


def convert_polygon_array_to_array_of_arrays(polygon_array):
    final_coords = []

    for coordinate_str in polygon_array:
        """
        -0.2071964 35.8474109
        """
        if coordinate_str == "":
            pass
        else:

            # final_coordinate_array = []

            coordinate_array = coordinate_str.split(" ")
            coordinate_array[0] = float(coordinate_array[0])
            coordinate_array[1] = float(coordinate_array[1])
            # print(coordinate_array)

            final_coordinate_array = [coordinate_array[1], coordinate_array[0]]

            final_coords.append(final_coordinate_array)

    # print(final_coords, "final_coords")

    if final_coords[-1] != final_coords[0]:
        final_coords.append(final_coords[0])

    return final_coords


def read_csv(file_path, command_str=""):
    logger.info("Reading CSV file: {}".format(file_path))

    # read csv file
    with open(file_path, "r") as csv_file:
        from accounts.models import SafaricomFarmer

        csv_reader = csv.reader(csv_file, delimiter=",")
        # skip header
        next(csv_reader)
        # iterate over rows
        count = 0
        for row in csv_reader:
            # create new account
            # print(row)
            """
            ['qnktqf', 'Rongai ', ' Nakuru', '-0.2072', '35.8474', '-0.2071964 35.8474109,-0.2072031 35.847412,-0.2071972 35.8474104,']
            """

            if count % 2000 == 0:
                logger.info("divisible by 1000, sleeping for ten secs")
                # sleep for 1 second
                logger.info("Sleeping for 1 second")
                time.sleep(2)

            count = count + 1

            if count >= 150000:
                break

            farmer_name = row[0]
            print(f"=============={count}- {farmer_name}===============")
            logger.info(f"=============={count}- {farmer_name}===============")

            if command_str == "update":
                farmer_name = row[1]
                logger.info(farmer_name, "updating...")

                try:
                    safaricom_farmer = SafaricomFarmer.objects.filter(
                        farmer_name=farmer_name
                    ).last()

                    if safaricom_farmer and safaricom_farmer.is_mapped == False:
                        safaricom_farmer.is_mapped = True
                        safaricom_farmer.save()
                        continue
                    else:
                        print("*******************farmer not found")
                        continue

                except Exception as e:
                    logger.info(e, "error getting the farmer")
                    continue

            location = row[1]
            county = row[2]
            latitude = float(row[3])
            longitude = float(row[4])

            try:
                safaricom_farmer_qs = SafaricomFarmer.objects.filter(
                    farmer_name=farmer_name,
                    county=county,
                    location=location,
                    location_pin=save_lat_lng_to_point(latitude, longitude),
                )

                # print(safaricom_farmer_qs, "safaricom_farmer_qs")

                if safaricom_farmer_qs.exists():
                    print("<<<<<<<<<<< already exists: Skipping")
                    logger.info("<<<<<<<<<<< already exists: Skipping")

                    # print new line
                    print("\n")
                    print("===============================")

                    continue

                else:
                    # create new account
                    # print(row)
                    # create new account
                    safaricom_farmer = SafaricomFarmer.objects.create(
                        farmer_name=farmer_name,
                        county=county,
                        location=location,
                        location_pin=save_lat_lng_to_point(latitude, longitude),
                    )
                    safaricom_farmer.save()
                    print("new account created")

            except SafaricomFarmer.DoesNotExist:

                safaricom_farmer = SafaricomFarmer.objects.update_or_create(
                    farmer_name=farmer_name,
                    location=location,
                    county=county,
                    location_pin=save_lat_lng_to_point(latitude, longitude),
                )

            polygon_str = row[5]
            """
            -0.2071964 35.8474109,-0.2072031 35.847412,-0.2071972 35.8474104
            """

            print(polygon_str, "polygon_str")

            if polygon_str == "" or polygon_str == 0 or len(polygon_str) <= 1:
                print("No polygon for {}".format(farmer_name))
                #  no polygon

                safaricom_farmer.has_errors = True
                safaricom_farmer.error_comments = (
                    f"Provided polygon cordinates: {polygon_str}"
                )

                safaricom_farmer.save()
                continue

            polygon_array = polygon_str.split(",")
            """
            ['-0.2071964 35.8474109', '-0.2072031 35.847412', '-0.2071972 35.8474104', ''] polygon array
            """

            if polygon_array[-1] == "":
                polygon_array.pop()

            if len(polygon_array) == 3 and polygon_array[0] != polygon_array[2]:
                # print((polygon_array), "TYPE 1")

                print(len(polygon_array), "should be three")

                polygon_array.append(polygon_array[0])

                try:
                    print(
                        polygon_array,
                        "<<<<  trying to save polygon array as Linestring",
                    )

                    x = convert_polygon_array_to_array_of_arrays(polygon_array)
                    # print(x, "x")
                    line = LineString(x)
                    # print(line, "line")
                except Exception as e:
                    print(e, "error converting ot Linestring")
                    continue

                try:
                    multi_line = MultiLineString(line)
                except Exception as e:
                    print(e, "error converting to MultiLineString")
                    continue

                try:

                    multi_line_to_polygon = multi_line.convex_hull
                    # print(
                    #     multi_line, "this is the multi line "
                    # )  # Returns a multilinestring
                    # print(
                    #     multi_line.convex_hull, "this is the convex "
                    # )  # Converts the multilinestring to polygon
                except Exception as e:
                    print(e, "convex hull error")
                    continue

                # safaricom_farmer.geom = multi_line
                safaricom_farmer = SafaricomFarmer.objects.filter(
                    farmer_name=farmer_name, has_errors=False
                ).last()
                try:
                    safaricom_farmer.boundary = multi_line_to_polygon
                except:
                    print("error saving boundary")
                    logger.info("error saving boundary")
                    continue

                safaricom_farmer.save()

            if len(polygon_array) < 4 and len(polygon_array) > 1:
                print(len(polygon_array), "Error: polygon array is too small")
                safaricom_farmer = SafaricomFarmer.objects.filter(
                    farmer_name=farmer_name, has_errors=False
                ).last()

                safaricom_farmer.has_errors = True
                try:
                    # print(
                    #     polygon_array, "<<<< trying to save polygon array as Linestring"
                    # )
                    line = LineString(
                        convert_polygon_array_to_array_of_arrays(polygon_array)
                    )
                except Exception as e:
                    print(e, "error convertint ot Linestring 1")
                    continue

                try:
                    multi_line = MultiLineString(line)
                except Exception as e:
                    print(e, "error converting to MultiLineString 1")
                    continue

                try:

                    multi_line_to_polygon = multi_line.convex_hull
                    # print(
                    #     multi_line, "this is the multi line "
                    # )  # Returns a multilinestring
                    # print(
                    #     multi_line.convex_hull, "this is the convex "
                    # )  # Converts the multilinestring to polygon
                    safaricom_farmer.boundary = multi_line_to_polygon
                except Exception as e:
                    print(e, "convex hull error 1")
                    continue

                safaricom_farmer.save()

            else:
                print("polygon length more than 3")
                print(polygon_array, "polygon array")
                print(len(polygon_array), "length of polygon array")

                try:
                    # print(
                    #     polygon_array, "<<<< trying to save polygon array as Linestring"
                    # )
                    line = LineString(
                        convert_polygon_array_to_array_of_arrays(polygon_array)
                    )
                except Exception as e:
                    print(e, "error convertint ot Linestring")
                    continue

                try:
                    multi_line = MultiLineString(line)
                except Exception as e:
                    print(e, "error converting to MultiLineString")
                    continue

                try:

                    multi_line_to_polygon = multi_line.convex_hull

                except Exception as e:
                    print(e, "convex hull error")
                    continue

                # safaricom_farmer.geom = multi_line
                safaricom_farmer = SafaricomFarmer.objects.filter(
                    farmer_name=farmer_name, has_errors=False
                ).last()

                try:
                    safaricom_farmer.boundary = multi_line_to_polygon
                except Exception as e:
                    print(e, "error saving boundary")
                    logger.info(e, "error saving boundary")

                    continue

                safaricom_farmer.save()

            # return final_coords
            if safaricom_farmer and safaricom_farmer.acreage == 0:
                area = round(
                    (
                        safaricom_farmer.boundary.area
                        * 12365.1613
                        * 10 ** 6
                        * 0.000247105
                    ),
                    2,
                )  # convert to acres
                # convert to acres

                print(area, "area")
                safaricom_farmer.acreage = area

                if area < (1 / 8):
                    safaricom_farmer.has_errors = True
                    safaricom_farmer.error_comments = (
                        f"Acreage error: Area less than one plot"
                    )

            if safaricom_farmer.boundary:
                point_in_polygon_bool = safaricom_farmer.boundary.contains(
                    safaricom_farmer.location_pin
                )

                if point_in_polygon_bool == False:
                    safaricom_farmer.has_errors = True
                    safaricom_farmer.error_comments = (
                        f"Acreage error: Location pin is not in polygon"
                    )

                safaricom_farmer.save()


if __name__ == "__main__":
    read_csv("./safdata.csv")
    # x = [
    #     "-0.2071964 35.8474109",
    #     "-0.2072031 35.847412",
    #     "-0.2071972 35.8474104",
    #     "-0.2071964 35.8474109",
    # ]
    # convert_polygon_array_to_array_of_arrays(x)
