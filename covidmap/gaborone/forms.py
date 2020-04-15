from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions, InlineCheckboxes
from .models import Patient
from django import forms

class PatientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'phone_number',
            Row(
                Column('age', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('symptoms', css_class='form-group col-md-6 mb-0'),
                Column('conditions', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('has_travelled', css_class='form-group col-md-6 mb-0'),
                Column('has_had_contact', css_class='form-group col-md-6 mb-0'),                
                css_class='form-row'
            ),
            Row(
                Column('has_tested', css_class='form-group col-md-6 mb-0'),
                Column('test_result', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('plot', css_class='form-group col-md-6 mb-0'),
                Column('region', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('save', 'Submit'),
            )
        )
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'symptoms': forms.CheckboxSelectMultiple,
            'conditions': forms.CheckboxSelectMultiple,
            } 
