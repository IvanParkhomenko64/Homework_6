from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterUser(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    # extra_context = {'is_active_register': 'active'}

    success_url = reverse_lazy('users:login')


def generate_new_password(request):
    request.user.set_password('54321')
    request.user.save()
    return redirect(reverse('users:login'))
