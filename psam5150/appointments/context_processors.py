# -*- coding: UTF-8 -*-
import datetime

from models import Contacts, Appointment

def counts(request):
    return {
        "num_contacts": Contacts.objects.all().count(),
        "num_events": Appointment.objects.all().count(),
        "events_today": Appointment.objects.filter(start_time=datetime.date.today()).count()

    }
