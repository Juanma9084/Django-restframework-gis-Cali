from django.contrib.gis.db.models.fields import MultiPolygonField
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from rest_framework import serializers

from geometrias.models import Comunas, Barrios


class IngenioSerializer(GeoFeatureModelSerializer):
    geom = GeometrySerializerMethodField()

    def get_geom(self, Comunas) -> MultiPolygonField:
        return Comunas.geom.transform(4326, clone=True)

    class Meta:
        model = Comunas
        geo_field = 'geom'
        fields = ['id_comuna',
                  'area_comuna',
                  'perimetro_comuna',
                  'geom',
                  ]


class HaciendaSerializer(GeoFeatureModelSerializer):
    geom = GeometrySerializerMethodField()

    def get_geom(self, Barrios) -> MultiPolygonField:
        return Barrios.geom.transform(4326, clone=True)

    class Meta:
        model = Barrios
        geo_field = 'geom'
        fields = ['id_barrio',
                  'id_comuna',
                  'nombre',
                  'area_barrio',
                  'perimetro_barrio',
                  'geom',
                  ]
