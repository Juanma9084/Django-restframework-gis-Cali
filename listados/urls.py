from django.urls import path

from listados.views import APIListadoComunas, APIListadoBarrios

urlpatterns = [
    path('comunas', APIListadoComunas.as_view()),
    path('barrios/', APIListadoBarrios.as_view()),
]
