from rest_framework import serializers

from listados.models import Comunas, Barrios


class ComunasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunas
        fields = ['id_comuna',
                  'area_comuna',
                  'perimetro_comuna'
                  ]


class BarriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrios
        fields = ['id_barrio',
                  'id_comuna',
                  'nombre',
                  'area_barrio',
                  'perimetro_barrio'
                  ]
