from django import forms
from .models import Patient


class PatientSignup(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_fname', 'patient_lname', 'patient_dob', 'patient_allergies', 'patient_street', 'patient_city','patient_state','patient_zip','patient_phone','patient_partially_vacc')
        required = ('patient_fname', 'patient_lname', 'patient_dob', 'patient_allergies', 'patient_phone','patient_partially_vacc')
        labels = {
        "patient_fname": "First Name",
        "patient_lname": "Last Name",
        "patient_dob": "Birthday",
        "patient_allergies": "Allergies?",
        "patient_phone": "Phone Number",
        "patient_partially_vacc":"Have you been vaccinated"
        }