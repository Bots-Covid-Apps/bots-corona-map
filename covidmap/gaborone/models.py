from django.db import models
from djgeojson.fields import PolygonField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class MapRegion(models.Model):
    region_name = models.CharField(max_length=200)
    current_cases = models.IntegerField(default=0)
    geom = PolygonField()

class Symptom(models.Model):
    description = models.CharField(max_length=100)

class Condition(models.Model):
    description = models.CharField(max_length=100)

class Support(models.Model):
    description = models.CharField(max_length=100)
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    phone_number = PhoneNumberField()
    region = models.ForeignKey('MapRegion', on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    symptoms = models.ManyToManyField(Symptom)
    condition = models.ManyToManyField(Condition)
    has_travelled = models.BooleanField()
    has_had_contact = models.BooleanField()
    has_tested = models.BooleanField(null=True, blank=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
