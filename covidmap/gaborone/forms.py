from crispy_forms.helper import FormHelper
from .models import Patient
from django import forms

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'symptoms': forms.CheckboxSelectMultiple,
            'conditions': forms.CheckboxSelectMultiple
            } 

