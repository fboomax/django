from django import forms
from .models import RegistrationData


class RegistrationForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100)
  email = forms.CharField(max_length=100)
  phone = forms.CharField(max_length=100)


class RegistrationModal(forms.ModelForm):
  class Meta:
    model = RegistrationData

    fields = [
      'username',
      'password',
      'email',
      'phone'
    ]

