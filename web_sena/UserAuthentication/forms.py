from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(
            attrs={'class': "form-control", 'placeholder': 'Nombre de Usuario'})
        self.fields['email'].widget = EmailInput(
            attrs={'class': "form-control", 'placeholder': 'Correo Electrónico'})
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': "form-control", 'placeholder': 'Confirmar Contraseña'})
