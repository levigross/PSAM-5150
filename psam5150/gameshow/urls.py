#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from views import GameMain, GameView

urlpatterns = patterns('',
    url(r'^$', GameMain.as_view(), name='game_main'),
    url(r'^game/$', GameView.as_view(), name='play_game'),
)

