import os

from osgeo import gdal
from osgeo.gdal import Translate

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path, "dir_path")

source_path = os.path.join(dir_path, "2019 08 13 Bendor NDVI_rgba_ndvi.tif")
destination_path = os.path.join(dir_path, "output.tif")


ds = gdal.Open(source_path)

# ds = gdal.Open('input.tif')
# ds = gdal.Translate('output.tif', ds, projWin = [-75.3, 5.5, -73.5, 3.7])

# gdal.Transformer
# ds1 = Transformer(source_path)
# ds = None
print(ds, "ds")

ds = gdal.Translate(destination_path, ds, maskBand=4)

if ds is None:
    print("fail")
else:
    print("Yes")

ds = None

# if ds.GetRasterBand(1).Checksum() != 21349:
#     # gdaltest.post_reason("Bad checksum")
#     print("Pass")


# Import gdal
# from osgeo import gdal

# #Open existing dataset
# src_ds = gdal.Open( src_filename )

# #Open output format driver, see gdal_translate --formats for list
# format = "GTiff"
# driver = gdal.GetDriverByName( format )

# #Output to new format
# dst_ds = driver.CreateCopy( dst_filename, src_ds, 0 )

# #Properly close the datasets to flush to disk
# dst_ds = None
# src_ds = None
