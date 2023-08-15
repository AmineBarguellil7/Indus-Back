from django.contrib.gis.db import models

class Polygone(models.Model):
    polygon = models.PolygonField()
