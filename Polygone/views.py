from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from .models import Polygone
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize
from django.http import HttpResponse

@api_view(['POST'])
def create_polygon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        location = data.get('location')
        if location:
            polygon_coords = [(coord[0], coord[1]) for coord in location]
            polygon_geom = Polygon(polygon_coords)
            polygon_obj = Polygone.objects.create(polygon=polygon_geom)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


@api_view(['GET'])
def get_all_polygons(request):
    if request.method == 'GET':
        polygons = Polygone.objects.all()
        polygons_json = serialize('json', polygons)
        return HttpResponse(polygons_json, content_type='application/json')

