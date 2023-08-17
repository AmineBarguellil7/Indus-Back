# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("create_polygon/", views.create_polygon, name="create_polygon"),
    path('get-all-polygons/', views.get_all_polygons, name='get_all_polygons'),
]
