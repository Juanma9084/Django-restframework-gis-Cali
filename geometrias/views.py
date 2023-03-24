from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from geometrias.models import Comunas, Barrios
from geometrias.serializers import IngenioSerializer, HaciendaSerializer


class APIGeometriasComunas(APIView):
    """Clase para el manejo de las peticiones a la base de datos de cedula canera

    Args:
        APIView ([type]): [description]
    """

    def get(self, request):
        try:
            comuna = request.query_params.get('comuna')

            comunas = Comunas.objects.filter(id_comuna=comuna).values(
                'id_comuna', 'area_comuna', 'perimetro_comuna').distinct('id_comuna')
            geometria = Comunas.objects.filter(
                id_comuna__in=comunas.values('id_comuna'), geom__isnull=False)

            serializer = IngenioSerializer(geometria, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class APIGeometriasBarrios(APIView):
    """Clase para el manejo de las peticiones a la base de datos de cedula canera

    Args:
        APIView ([type]): [description]
    """

    def get(self, request):
        try:
            barrio = request.query_params.get('barrio')

            hacienda = Barrios.objects.filter(id_barrio=barrio).values(
                'id_barrio', 'id_comuna', 'nombre', 'area_barrio', 'perimetro_barrio',).distinct('id_barrio')
            geometria = Barrios.objects.filter(
                id_barrio__in=hacienda.values('id_barrio'), geom__isnull=False)

            serializer = HaciendaSerializer(geometria, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
