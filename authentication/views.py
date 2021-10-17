# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/index_admin")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            email = form.cleaned_data.get("email")     
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")          
            user = authenticate(username=username, password=raw_password)
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form})




