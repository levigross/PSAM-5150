# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from views import WelcomePage, BookAnAppointment, AddContact, AddEventType
urlpatterns = patterns('',
    url(r'^$', WelcomePage.as_view(), name='appointment_welcome_page'),
    url(r'^book/$', BookAnAppointment.as_view(), name='book_appointment'),
    url(r'^contact/$', AddContact.as_view(), name='add_contact'),
    url(r'^event_type/$', AddEventType.as_view(), name='add_event'),
)
