from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserModel,
                                       AuthenticationForm)
from .models import Account


class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'password1', 'first_name', 'last_name']


class AuthenticationForm1(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
