# -*- coding: UTF-8 -*-
from django import forms
from models import Appointment

class AppointmentModelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['event_type', 'title', 'description', 'guests', 'start_time', 'end_time']
        fieldsets = (('event_title', {'fields': ('title', ),
                                      'description': 'The name of your event',
                                      'legend': 'Title', }),
                     ('event_details', {'fields': ('description', 'start_time', 'end_time',),
                                        'description': 'Tell me about your event',
                                        'legend': 'About Your Event'}),
                     ('event_guests', {'fields': ('guests',),
                                       'description': 'Do you want to invite someone?',
                                       'legend': 'Guests'}),
            )
