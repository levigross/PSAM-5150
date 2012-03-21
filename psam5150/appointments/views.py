from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages

from forms import AppointmentModelForm
from models import Contacts, EventType


class WelcomePage(TemplateView):
    template_name = 'appointments/welcome.html'


class BookAnAppointment(CreateView):
    form_class = AppointmentModelForm
    template_name = 'appointments/form.html'


    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your submission is complete")
        super(BookAnAppointment, self).get_success_url()


class AddContact(CreateView):
    model = Contacts
    template_name = 'appointments/form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your contact has been added")
        super(AddContact, self).get_success_url()

class AddEventType(CreateView):
    model = EventType
    template_name = 'appointments/form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your Event Type has been added")
        super(AddEventType, self).get_success_url()
