from django.db import models

# Create your models here.
class Results(models.Model):
    base_file = models.FileField(upload_to='files/')
    ebazr_file = models.FileField(upload_to='files/')
    vendor_file = models.FileField(upload_to='files/')
    result_file = models.FileField(null=True,upload_to='files/')
    basemap_file = models.FileField(null=True,upload_to='files/')

