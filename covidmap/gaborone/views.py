from .models import Patient
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper

# Create your views here.
class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
