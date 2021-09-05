from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.db.models.signals import post_save

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PlotDetail(models.Model):
    class Meta:
        verbose_name = "Plot Detail"
        verbose_name_plural = "Plot Detail"

    farm = models.ForeignKey("accounts.Farmer", on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=True, null=True)

    acreage = models.FloatField(default=0)
    boundary = gis_models.PolygonField(blank=True, null=True)
    tiles = models.URLField(blank=True, null=True)

    crop = models.ForeignKey(
        "farm.FarmCrop", on_delete=models.CASCADE, blank=True, null=True
    )
    last_crop_yield = models.FloatField(default=0)

    spray_detail = models.ManyToManyField("farm.SprayDetail", blank=True)

    def __str__(self):
        return self.name


class PlotMap(gis_models.Model):
    plot_detail = models.ForeignKey("farm.PlotDetail", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    RGB = "RGB"
    NDVI = "NDV"
    MAP_CHOICES = [
        (RGB, "RGB Map"),
        (NDVI, "NDVI Map"),
    ]
    map_type = models.CharField(
        max_length=4,
        choices=MAP_CHOICES,
        default=RGB,
    )
    uploaded_tif = models.FileField(upload_to="uploads/", blank=True, null=True)
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    # upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    raster = gis_models.RasterField(blank=True, null=True)

    def __str__(self):
        return self.name


# post-save signal to convert geotif to raster
def convert_tif_to_raster(sender, instance, created, **kwargs):
    if instance.uploaded_tif:
        print(instance.uploaded_tif.path, "instance.upload_tif.path")
        print(instance.uploaded_tif.url, "instance.upload_tif.url")

        # instance.raster = instance.uploaded_tif.path
        # instance.uploaded_tif.delete()

        # Read a raster as a file object from a remote source.
        from urllib.request import urlopen

        full_url = f"http://127.0.0.1:8000{instance.uploaded_tif.url}"
        print(full_url, "full_url")

        dat = urlopen(full_url).read()
        print(dat, "dat")

        from django.contrib.gis.gdal import GDALRaster

        # from myapp.models import RasterWithName
        gdal_raster = GDALRaster(dat)
        # rast = RasterWithName(name="one", raster=gdal_raster)
        # rast.save()
        print(gdal_raster.name, "gdal_raster.name")

        instance.raster = gdal_raster

        # GDALRaster django model

    if instance.uploaded_tif == "":
        instance.raster = None

    instance.save()


post_save.connect(convert_tif_to_raster, sender=PlotMap)
# import post_save signal django

CROP = (
    ("MZE", "Maize"),
    ("WHT", "Wheat"),
    ("BLY", "Barley"),
    ("CNL", "Canola"),
    ("TEA", "Tea"),
    ("CFE", "Coffee"),
    ("AVD", "Avocado"),
    ("BNA", "Banana"),
    ("OTH", "Other"),
)

PEST = (
    ("FAW", "Fall Army Worm"),
    ("APD", "Aphids"),
    ("CTW", "Cutworms"),
    ("TRP", "Thrips"),
    ("WVL", "Weevils"),
    ("WTF", "Whiteflies"),
    ("MTE", "Mites"),
    ("OTH", "Other"),
)

CHEMICAL_TYPE = (
    ("FGC", "Fungicide"),
    ("IST", "Insecticide"),
    ("FLR", "Foliar"),
    ("RND", "Roundup"),
    ("OTH", "Other"),
)

DISEASE = (
    ("RST", "Rust"),
    ("BST", "Black Spot"),
    ("FSW", "Fusarium Wilt"),
    ("OTH", "Other"),
)


class FarmCrop(models.Model):
    class Meta:
        verbose_name = "Farm Crop"
        verbose_name_plural = "Farm Crops"

    crop = models.CharField(choices=CROP, max_length=3)
    other = models.CharField(max_length=30, blank=True, null=True)
    crop_variety = models.CharField(max_length=30)
    crop_planted_date = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    last_crop_yield = models.FloatField(default=0)
    seed_company = models.ForeignKey("accounts.SeedCompany", on_delete=models.CASCADE)

    def __str__(self):
        return self.crop


class FarmPest(models.Model):
    class Meta:
        verbose_name = "Farm Pest"
        verbose_name_plural = "Farm Pests"

    pest = models.CharField(choices=PEST, max_length=3)
    other = models.CharField(max_length=30, blank=True, null=True)
    plot_detail = models.ForeignKey("farm.PlotDetail", on_delete=models.CASCADE)
    acreage_infested = models.FloatField(default=0)
    last_treated_date = models.DateTimeField(blank=True, null=True)
    spray_details = models.ManyToManyField("farm.SprayDetail", blank=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FarmDisease(models.Model):
    class Meta:
        verbose_name = "Farm Disease"
        verbose_name_plural = "Farm Diseases"

    name = models.CharField(choices=DISEASE, max_length=3)
    other = models.CharField(max_length=30, blank=True, null=True)
    plot_detail = models.ForeignKey("farm.PlotDetail", on_delete=models.CASCADE)
    acreage_infested = models.FloatField(default=0)
    last_treated_date = models.DateTimeField(blank=True, null=True)
    spray_details = models.ManyToManyField("farm.SprayDetail", blank=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Chemical(models.Model):
    class Meta:
        verbose_name = "Chemical"
        verbose_name_plural = "Chemicals"

    name = models.CharField(max_length=30)
    chemical_type = models.CharField(choices=CHEMICAL_TYPE, max_length=3)
    other = models.CharField(max_length=30, blank=True, null=True)

    recommended_dosage_per_ha = models.FloatField(default=0)

    manufacturer = models.ForeignKey(
        "accounts.ChemicalCompany",
        on_delete=models.CASCADE,
        related_name="chemical_manufacturer",
    )
    reseller = models.ForeignKey(
        "accounts.ChemicalCompany",
        on_delete=models.CASCADE,
        related_name="chemical_reseller",
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)
    container_image = models.ImageField(
        upload_to="uploads/chemicals/labels/", blank=True, null=True
    )

    def __str__(self):
        return self.name


class SprayDetail(models.Model):
    class Meta:
        verbose_name = "Spray Detail"
        verbose_name_plural = "Spray Details"

    farm_detail = models.ForeignKey("farm.PlotDetail", on_delete=models.CASCADE)
    acreage_spayed = models.FloatField(default=0)
    chemicals_sprayed = models.ManyToManyField("farm.Chemical")

    date_sprayed = models.DateTimeField()

    def __str__(self):
        return str(self.date_sprayed)


def save_spray_to_farm_many_to_many(sender, instance, created, **kwargs):

    farm = instance.farm_detail
    print(farm, "farm")
    print(farm.spray_detail, "farm.spray_details")
    farm.spray_detail.add(instance)
    print(farm.spray_detail, "farm.spray_details")

    farm.save()
    print(farm, "farm")


post_save.connect(save_spray_to_farm_many_to_many, sender=SprayDetail)
