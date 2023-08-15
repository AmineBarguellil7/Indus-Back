# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("create_polygon/", views.create_polygon, name="create_polygon"),
]
