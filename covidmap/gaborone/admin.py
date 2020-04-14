from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Symptom)
admin.site.register(Condition)
admin.site.register(Support)
admin.site.register(Patient)
admin.site.register(MapRegion)