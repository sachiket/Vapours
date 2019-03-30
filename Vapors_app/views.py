from django.shortcuts import render
from django.urls import reverse_lazy #for url navigaton
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #redirect to login page
    template_name = 'accounts/signup.html'
