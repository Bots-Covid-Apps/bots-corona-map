from django.db import models
from djgeojson.fields import PolygonField

# Create your models here.
class MapRegion(models.Model):
    region_name = models.CharField(max_length=200)
    current_cases = models.IntegerField(default=0)
    geom = PolygonField()
    
    