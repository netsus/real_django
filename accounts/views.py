from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/form.html"
    success_url = settings.LOGIN_URL


signup = SignUpView.as_view()


class MyLoginView(LoginView):
    template_name = "accounts/form.html"


login = MyLoginView.as_view()


class MyLogoutView(LogoutView):
    pass
