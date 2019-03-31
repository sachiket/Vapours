import csv
from django.shortcuts import render, redirect
from django.urls import reverse_lazy #for url navigaton
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import forms
from . import models
from .models import BlogComments
from .forms import BlogCommentsForm
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #redirect to login page
    template_name = 'accounts/signup.html'



def showform(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context= {'form': form }

    return render(request, 'accounts/qform.html',context)




def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'

    writer = csv.writer(response)
    writer.writerow(['f1', 'f2', 'f3', 'f4','f5', 'f6', 'f7', 'f8','f9', 'f10', 'f11', 'f12','f13', 'f14', 'f15', 'f16','f17', 'f18', 'f19', 'f20','f21', 'f22', 'f23', 'f24','f25', 'f26', 'f27'])

    users = BlogComments.objects.all()
    for obj in users:
        writer.writerow([obj.f1 ,obj.f2, obj.f3, obj.f4, obj.f5,obj.f6 ,obj.f7, obj.f8, obj.f9, obj.f10,obj.f11 ,obj.f12, obj.f13, obj.f14, obj.f15,obj.f16 ,obj.f17, obj.f18, obj.f19, obj.f20,obj.f21 ,obj.f22, obj.f23, obj.f24, obj.f25, obj.f26, obj.f27])

    return response



# class demo(CreateView):
#     form_class = forms.UserForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/qform.html'
