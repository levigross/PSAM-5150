#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import Host,Game,Player

admin.site.register(Host)
admin.site.register(Game)
admin.site.register(Player)
