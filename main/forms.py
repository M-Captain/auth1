from django import forms
from .models import Auth

class SignupForm(forms.ModelForm):
    class Meta:
        model=Auth
        fields="__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model=Auth
        fields= "email","password"
