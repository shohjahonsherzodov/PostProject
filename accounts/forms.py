from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomi")
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
