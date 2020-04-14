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
    
    def __str__(self):
        return self.description

class Condition(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Support(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    phone_number = PhoneNumberField("Phone Number")
    plot =  models.IntegerField("Plot Number", null=True, blank=True)
    region = models.ForeignKey('MapRegion', on_delete=models.CASCADE)
    age = models.IntegerField(default=0, help_text="Age of Person")
    symptoms = models.ManyToManyField(Symptom, help_text="Current Symptoms")
    conditions = models.ManyToManyField(Condition, help_text="Patients Pre-exsisting Condition")
    has_travelled = models.BooleanField(help_text="Has the patient travled to an affected area")
    has_had_contact = models.BooleanField(help_text="Has the patient had contact with anyone with the virus")
    has_tested = models.BooleanField(null=True, blank=True, help_text="Has the patient been tested and what is the result")
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
