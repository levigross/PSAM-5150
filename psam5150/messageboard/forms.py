# -*- coding: UTF-8 -*-
from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100, widget=PasswordInput)
