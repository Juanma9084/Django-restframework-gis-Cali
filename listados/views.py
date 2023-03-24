from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from listados.models import Comunas, Barrios
from listados.serializers import ComunasSerializer, BarriosSerializer


class APIListadoComunas(APIView):
    """Clase para el manejo de las peticiones a la base de datos de cedula canera

    Args:
        APIView ([type]): [description]
    """

    def get(self, request):
        try:
            # cod_ingenios = ParametrizacionIngenio.objects.all().order_by('codigo_ingenio')
            cod_comuna = Comunas.objects.all().order_by('id_comuna')
            serializer = ComunasSerializer(
                cod_comuna, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class APIListadoBarrios(APIView):
    """Clase para el manejo de las peticiones a la base de datos de cedula canera

    Args:
        APIView ([type]): [description]
    """

    def get(self, request):
        try:
            comuna = request.query_params.get('comuna')

            # ingenio = ParametrizacionHaciendas.objects.filter(codigo_ingenio = ingenios).values('id_archivo').first()
            barrio = Barrios.objects.filter(
                id_comuna=comuna).order_by('id_barrio')

            serializer = BarriosSerializer(barrio, many=True)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
