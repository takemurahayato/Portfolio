from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.shortcuts import render

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"

class IndexView(TemplateView):
    template_name = "top.html"

