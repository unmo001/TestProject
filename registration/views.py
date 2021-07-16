from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
from registration.forms import LoginForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class Logout(LoginRequiredMixin,LogoutView):
    template_name = 'registration/login.html'


