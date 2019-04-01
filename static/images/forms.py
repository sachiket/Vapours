
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import RadioSelect
from choicebtn.models import myChoice
from django import forms
from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

        name=forms.CharField(max_length=55)
        TYPE_SELECT = (('0', 'Female'),('1', 'male'),)
        gender=forms.ChoiceField(widgets.RadioSelect(choices=TYPE_SELECT))


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

        model = myChoice
        fields = ['name','gender']
