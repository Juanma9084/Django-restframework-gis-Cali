from django.contrib.gis.db import models


class Comunas(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    area_comuna = models.DecimalField(
        max_digits=12, decimal_places=0, blank=True, null=True)
    perimetro_comuna = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    geom = models.MultiPolygonField(srid=3115, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalizado\".\"comunas'


class Barrios(models.Model):
    id_barrio = models.CharField(primary_key=True, max_length=4)
    id_comuna = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    area_barrio = models.DecimalField(
        max_digits=12, decimal_places=0, blank=True, null=True)
    perimetro_barrio = models.DecimalField(
        max_digits=12, decimal_places=0, blank=True, null=True)
    geom = models.MultiPolygonField(srid=3115, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalizado\".\"barrios'
