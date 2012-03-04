#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from django import forms

TEAM_CHOICES = (
    ('T1', 'Team One',),
    ('T2', 'Team Two',)
    )

class GameScore(forms.Form):
    team = forms.ChoiceField(choices=TEAM_CHOICES)
    score = forms.IntegerField()
