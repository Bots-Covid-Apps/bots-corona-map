from .forms import PatientForm
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper

# Create your views here.
class PatientCreateView(CreateView):
    form_class = PatientForm
    template_name = "gaborone/patient_form.html"
