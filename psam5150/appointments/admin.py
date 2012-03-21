# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import Appointment, Contacts, EventType

class EventTypeAdmin(admin.ModelAdmin):
    pass


class ContactsAdmin(admin.ModelAdmin):
    pass


class AppointmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
