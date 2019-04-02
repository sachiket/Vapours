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
import numpy as np

# import .scripts import suicide_pred_dup
from . import suicide_pred
from . import phq_pred

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
    phq1 = []
    phq2 = []
    phq3 = []
    phq4 = []
    phq5 = []
    phq6 = []
    phq7 = []
    phq8 = []
    phq9 = []
    params = []
    if form.is_valid():
        form.save()

        phq1.append(int(form.cleaned_data['PHQ1A']))
        phq1.append(int(form.cleaned_data['PHQ1B']))
        phq1.append(int(form.cleaned_data['PHQ1C']))
        phq1.append(int(form.cleaned_data['PHQ1D']))
        phq9.append(int(form.cleaned_data['PHQ9']))
        phq6.append(int(form.cleaned_data['PHQ6A']))
        phq6.append(int(form.cleaned_data['PHQ6B']))
        phq6.append(int(form.cleaned_data['PHQ6C']))
        phq6.append(int(form.cleaned_data['PHQ6D']))
        phq2.append(int(form.cleaned_data['PHQ2A']))
        phq2.append(int(form.cleaned_data['PHQ2B']))
        phq2.append(int(form.cleaned_data['PHQ2C']))
        phq3.append(int(form.cleaned_data['PHQ3']))
        phq4.append(int(form.cleaned_data['PHQ4A']))
        phq4.append(int(form.cleaned_data['PHQ4B']))
        phq4.append(int(form.cleaned_data['PHQ4C']))
        phq8.append(int(form.cleaned_data['PHQ8']))
        phq5.append(int(form.cleaned_data['PHQ5']))
        phq7.append(int(form.cleaned_data['PHQ7A']))
        phq7.append(int(form.cleaned_data['PHQ7B']))
        phq7.append(int(form.cleaned_data['PHQ7C']))
        phq7.append(int(form.cleaned_data['PHQ7D']))
        # name = form.cleaned_data['Name']
        # print(name)

        phq1_df_test = np.array(phq1).reshape([1, 4])
        phq2_df_test = np.array(phq2).reshape([1, 3])
        phq3_df_test = np.array(phq3).reshape([1, 1])
        phq4_df_test = np.array(phq4).reshape([1, 3])
        phq5_df_test = np.array(phq5).reshape([1, 1])
        phq6_df_test = np.array(phq6).reshape([1, 4])
        phq7_df_test = np.array(phq7).reshape([1, 4])
        phq8_df_test = np.array(phq8).reshape([1, 1])
        phq9_df_test = np.array(phq9).reshape([1, 1])
        phq_score, dep = phq_pred.phq_preqiction(phq1_df_test, phq2_df_test, phq3_df_test, phq4_df_test, phq5_df_test, phq6_df_test, phq7_df_test, phq8_df_test, phq9_df_test)
        dep = 1 if dep == True else 0


        params.append(int(form.cleaned_data['Gender']))
        params.append(int(form.cleaned_data['Sexuality']))
        params.append(int(form.cleaned_data['Age']))
        params.append(int(form.cleaned_data['Body_weight']))
        params.append(int(form.cleaned_data['Virgin']))
        params.append(int(form.cleaned_data['Prostitution_legal']))
        params.append(int(form.cleaned_data['Pay_for_sex']))
        params.append(int(form.cleaned_data['Friends']))
        params.append(int(form.cleaned_data['Social_fear']))
        params.append(dep)

        pred = suicide_pred.svm_test(test = np.array(params).reshape([1, 10]))
        pred = "Yes" if pred == 1 else "No"
        
        print(phq_score, dep)
        print(pred)
        return redirect('home')

    context= {'form': form }

    return render(request, 'accounts/qform.html',context)

def csv_training(user_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name','Age','Gender','Sexuality','Bodyweight','Virgin','Prostitution_legal','Pay_for_sex','Friends','Social_fear','PHQ1A','PHQ1B','PHQ1C','PHQ9','PHQ6A','PHQ6B','PHQ6C','PHQ6D','PHQ2A','PHQ2B','PHQ2C','PHQ3','PHQ4A','PHQ4B','PHQ4C','PHQ8','PHQ9','PHQ7A','PHQ7B','PHQ7C','PHQ7D'])

    users = Blog.objects.all()
    for obj in users:
        if(obj.Name == user_name):
            writer.writerow([obj.Name,obj.Age,obj.Gender,obj.Sexuality,obj.Body_weight,obj.Virgin,obj.Prostitution_legal,obj.Pay_for_sex,obj.Friends,obj.Social_fear,obj.PHQ1A ,obj.PHQ1B, obj.PHQ1C, obj.PHQ9, obj.PHQ6A,obj.PHQ6B ,obj.PHQ6C, obj.PHQ6D, obj.PHQ2A, obj.PHQ2B,obj.PHQ2C ,obj.PHQ3, obj.PHQ4A, obj.PHQ4B, obj.PHQ4C,obj.PHQ8 ,obj.PHQ5, obj.PHQ7A, obj.PHQ7B, obj.PHQ7C,obj.PHQ7D])

    return response


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
