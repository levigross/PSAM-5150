# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import patterns, url
from views import MainPage, Login

urlpatterns = patterns('',
    url(r'^$', login_required(MainPage.as_view()) ,name='loginmainpage'),
    url(r'^login/$', Login.as_view()),
)


