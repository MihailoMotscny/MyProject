from django.contrib.auth.views import LoginView

from .models import Artiles
from django.forms import ModelForm,TextInput,DateTimeInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['name_company','culture','price','date']

        widgets = {
            "name_company":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Назва компанії'
            }),

            "culture": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Культура'
            }),

            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })

        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": TextInput(attrs={

                'placeholder': 'Імя користувача'
            }),

            "password1": TextInput(attrs={

                'placeholder': 'Пароль'
            }),

            "password2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Підтвердження паролю'
            })
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)