from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from forms import LoginForm

class MainPage(TemplateView):
    template_name = 'messageboard/welcome.html'

    def get_context_data(self, **kwargs):
        return {
            'message': "Hello %s" % self.request.user.first_name,
            }



class Login(TemplateView):
    template_name = 'messageboard/login.html'

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return self.get(request, login_form=login_form)
        username = login_form.cleaned_data['user_name']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('loginmainpage')
            else:
                pass # Account inactive
        else:
            pass #Wrong username and password

    def get_context_data(self, **kwargs):
        return {
            'login_form':LoginForm() if not kwargs.get('login_form', None) else kwargs['login_form'] ,
        }
