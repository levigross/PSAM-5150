# -*- coding: UTF-8 -*-
from django import forms

from signupform.models import Signup

class HelloWorldForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'email', 'reason_for_joining', 'picture', 'url']
