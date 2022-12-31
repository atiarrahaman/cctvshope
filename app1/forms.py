from django import forms 
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdressForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','location','distric','zipcode','division']

class Singupform(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1','password2']