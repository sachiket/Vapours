import csv
from django.shortcuts import render, redirect
from django.urls import reverse_lazy #for url navigaton
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import forms
from . import models
from .models import Blog
from .forms import BlogCommentsForm
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #redirect to login page
    template_name = 'accounts/signup.html'



def showform(request):
    form= BlogCommentsForm(request.POST or None)
    # form2=BlogCommentsForm.request.get(value)
    #print(form)
    phq_list = []
    if form.is_valid():
        phq_list.append(form.cleaned_data['PHQ1A'])
        phq_list.append(form.cleaned_data['PHQ1B'])
        phq_list.append(form.cleaned_data['PHQ1C'])
        phq_list.append(form.cleaned_data['PHQ1D'])
        phq_list.append(form.cleaned_data['PHQ9'])
        phq_list.append(form.cleaned_data['PHQ6A'])
        phq_list.append(form.cleaned_data['PHQ6B'])
        phq_list.append(form.cleaned_data['PHQ6C'])
        phq_list.append(form.cleaned_data['PHQ6D'])
        phq_list.append(form.cleaned_data['PHQ2A'])
        phq_list.append(form.cleaned_data['PHQ2B'])
        phq_list.append(form.cleaned_data['PHQ2C'])
        phq_list.append(form.cleaned_data['PHQ3'])
        phq_list.append(form.cleaned_data['PHQ4A'])
        phq_list.append(form.cleaned_data['PHQ4B'])
        phq_list.append(form.cleaned_data['PHQ4C'])
        phq_list.append(form.cleaned_data['PHQ8'])
        phq_list.append(form.cleaned_data['PHQ5'])
        phq_list.append(form.cleaned_data['PHQ7A'])
        phq_list.append(form.cleaned_data['PHQ7B'])
        phq_list.append(form.cleaned_data['PHQ7C'])
        phq_list.append(form.cleaned_data['PHQ7D'])
        print(phq_list)



        form.save()
        return redirect('home')

    context= {'form': form }

    return render(request, 'accounts/qform.html',context)




def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name','Age','Gender','Sexuality','Bodyweight','Virgin','Prostitution_legal','Pay_for_sex','Friends','Social_fear','PHQ1A','PHQ1B','PHQ1C','PHQ9','PHQ6A','PHQ6B','PHQ6C','PHQ6D','PHQ2A','PHQ2B','PHQ2C','PHQ3','PHQ4A','PHQ4B','PHQ4C','PHQ8','PHQ9','PHQ7A','PHQ7B','PHQ7C','PHQ7D'])

    users = Blog.objects.all()
    for obj in users:
        writer.writerow([obj.Name,obj.Age,obj.Gender,obj.Sexuality,obj.Body_weight,obj.Virgin,obj.Prostitution_legal,obj.Pay_for_sex,obj.Friends,obj.Social_fear,obj.PHQ1A ,obj.PHQ1B, obj.PHQ1C, obj.PHQ9, obj.PHQ6A,obj.PHQ6B ,obj.PHQ6C, obj.PHQ6D, obj.PHQ2A, obj.PHQ2B,obj.PHQ2C ,obj.PHQ3, obj.PHQ4A, obj.PHQ4B, obj.PHQ4C,obj.PHQ8 ,obj.PHQ5, obj.PHQ7A, obj.PHQ7B, obj.PHQ7C,obj.PHQ7D])

    return response



# class demo(CreateView):
#     form_class = forms.UserForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/qform.html'
