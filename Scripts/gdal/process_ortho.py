import os

import gdal2tiles

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path, "dir_path")


source_path = os.path.join(dir_path, "twiga_transparent_mosaic_group1.tif")
destination_path = os.path.join(dir_path, "output_rgb")


def create_tiles(source_path, destination_path):

    """
    Method to generate tiles at different zoom levels using gdal2tiles library.
    Args:
    1. source_path :
        path for the source file which needs to be tiled
    2. destination_path :
        path for the output directory where the tiles will be generated
    3. Options:
        profile (str): Tile cutting profile (mercator,geodetic,raster) - default
            'mercator' (Google Maps compatible)
        resampling (str): Resampling method (average,near,bilinear,cubic,cubicsp
            line,lanczos,antialias) - default 'average'

        s_srs: The spatial reference system used for the source input data

        zoom: Zoom levels to render; format: '[int min, int max]',
            'min-max' or 'int/str zoomlevel'.

        tile_size (int): Size of tiles to render - default 256

        resume (bool): Resume mode. Generate only missing files.

        srcnodata: NODATA transparency value to assign to the input data

        tmscompatible (bool): When using the geodetic profile, specifies the base
            resolution as 0.703125 or 2 tiles at zoom level 0.

        verbose (bool): Print status messages to stdout

        kml (bool): Generate KML for Google Earth - default for 'geodetic'
            profile and 'raster' in EPSG:4326. For a dataset with different projection use with caution!

        url (str): URL address where the generated tiles are going to be published

        webviewer (str): Web viewer to generate (all,google,openlayers,none) -
            default 'all'

        title (str): Title of the map

        copyright (str): Copyright for the map

        googlekey (str): Google Maps API key from
            http://code.google.com/apis/maps/signup.html

        bingkey (str): Bing Maps API key from https://www.bingmapsportal.com/

        nb_processes (int): Number of processes to use for tiling.

    """
    options = {
        "zoom": (10, 17),
        "nb_processes": 2,
        "tile_size": 256,
        "srs": "EPSG:4326",
        "title": "test script",
        "resume": True,
        "srcnodata": "0",
    }
    gdal2tiles.generate_tiles(source_path, destination_path, **options)


if __name__ == "__main__":
    create_tiles(source_path, destination_path)
