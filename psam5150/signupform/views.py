from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from signupform.forms import HelloWorldForm, SignupForm
from signupform.models import HelloWorld


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def signuphome(request):
    oursite = get_current_site(request)
    return render_to_response('signup/main.html', {'title': oursite.name}, context_instance=RequestContext(request))


def helloworld(request):
    if request.method == 'POST':
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            our_hello_world = HelloWorld()
            our_hello_world.name = form.cleaned_data['name']
            our_hello_world.location = form.cleaned_data['location']
            our_hello_world.message = form.cleaned_data['message']
            our_hello_world.save()
            return redirect('hello')
    else:
        form = HelloWorldForm()
    return render_to_response('signup/helloworld.html', {'form': form}, context_instance=RequestContext(request))


def hello(request):
    last_hellos = HelloWorld.objects.all().order_by('-created_on')
    return render_to_response('signup/hello.html', {'hellos': last_hellos}, context_instance=RequestContext(request))


def sitesignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            form.save()
            messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
            return redirect('signup_main')
    else:
        form = SignupForm()
    return render_to_response('signup/signup.html', {'form': form}, context_instance=RequestContext(request))
