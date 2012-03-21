# -*- coding: UTF-8 -*-
from django import forms
from models import Appointment

class AppointmentModelForm(forms.ModelForm):

    class Meta:
        model = Appointment

