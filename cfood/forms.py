from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password", "email"]

class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
