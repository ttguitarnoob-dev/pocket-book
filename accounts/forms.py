
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

        widget = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'password': forms.TextInput(attrs = {'class': 'form-control'}),
            'confirm_password': forms.TextInput(attrs = {'class': 'form-control'}),
        }