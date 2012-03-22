from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class EventType(models.Model):
    event_name = models.CharField(max_length=100, help_text="This is the name of of your event type")

    class Meta:
        verbose_name_plural = 'Event Types'

    def __unicode__(self):
        return self.event_name

class Appointment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    event_type = models.ForeignKey('EventType', unique=True, related_name="EventType")
    title = models.CharField(max_length=100)
    description = models.TextField()
    guests = models.ManyToManyField('Contacts', related_name="contacts")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Appointments'

    def __unicode__(self):
        return self.title

class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField()
    phone_number = PhoneNumberField()

    class Meta:
        verbose_name_plural = "Contacts"

    def __unicode__(self):
        return u"%s %s" % (self.name, self.email_address)

    @property
    def name(self):
        return u"%s %s" % (self.first_name, self.last_name)

