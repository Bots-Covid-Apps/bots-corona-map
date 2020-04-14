from .forms import PatientForm
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper
from django.urls import reverse


# Create your views here.
class PatientCreateView(CreateView):
    template_name = "gaborone/patient_form.html"
    form_class = PatientForm
    success_url = '/'
