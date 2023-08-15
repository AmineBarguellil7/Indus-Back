from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from .models import Polygone
from django.contrib.gis.geos import Polygon

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
