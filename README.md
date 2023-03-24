# API Para la consulta de informacion cartografica - Django-restframework-gis-Cali

API de la información de la cuidad de Cali.
Esta interfaz de programación de aplicaciones ***API*** recoge los datos de una base de datos de la ciudad de Cali


## Instalacion de las librerias requeridas

```
pip install -r requerimientos.txt
```

## Para correr servidor

```
python manage.py runserver
```

## Uso

**API**

Generación de listados con http://127.0.0.1:8000/listados/comunas

Generación de geometrías con http://127.0.0.1:8000/geometrias/comunas?comuna=02

### Creación de listados
Se crea el modelo con el ```python manage.py inspectdb > model.py```, se definen las URL's y los serializadores, yal final se edita el archivo view.py de la siguiente forma:
```py
    def get(self, request):
        try:
            cod_comuna = Comunas.objects.all().order_by('id_comuna')
            serializer = ComunasSerializer(
                cod_comuna, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```
### Creación de las geometrias
Igual que los listados, se editan los modelos, las URL's, los serializadores y al final se edita el archivo view.py de la siguiente forma:
```py
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
```
