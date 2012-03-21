"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import EventType, Appointment, Contacts

class SimpleTest(TestCase):
    def setUp(self):
        raise NotImplementedError

    def testEventType(self):
        raise NotImplementedError

    def testAppointment(self):
        raise NotImplementedError

    def testContacts(self):
        raise NotImplementedError
