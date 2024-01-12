from django.contrib.gis.db import models


class Public(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    wkb_geometry = models.MultiPolygonField(srid=32639, spatial_index=True)
    fid = models.DecimalField(max_digits=10, decimal_places=0)
    navahi = models.DecimalField(max_digits=10, decimal_places=0)
    area = models.FloatField()
    fid1 = models.DecimalField(max_digits=10, decimal_places=0)
    latlon = models.CharField(max_length=255)
    nahieid = models.FloatField()
    name = models.CharField(max_length=255)
    population = models.FloatField()
    objectid = models.FloatField()
    unqid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pg_dump'