# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='إسم المستخدم',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    password = forms.CharField(label='كلمة المرور',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='إسم المستخدم',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(label='الإسم',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(label='اللقب',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    email = forms.EmailField(label='الإيميل',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(label='كلمة المرور',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

