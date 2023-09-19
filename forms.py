from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['email', 'name', 'registration_number', 'password', 'mobile_number']