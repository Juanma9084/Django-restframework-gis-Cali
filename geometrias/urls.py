from django.urls import path

from geometrias.views import APIGeometriasComunas, APIGeometriasBarrios

urlpatterns = [
    path('comunas/', APIGeometriasComunas.as_view()),
    path('barrios/', APIGeometriasBarrios.as_view()),
]
