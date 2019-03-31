
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import RadioSelect
# from .models import Order
from django import forms
from django.contrib.auth.models import User
from .models import BlogComments



FCHOICES= [
    ('Low', 'Low'),
    ('Moderate', 'Moderate'),
    ('High', 'High'),
    ]
aCHOICES= [
    ('Not at all', 'Not at all'),
    ('Several', 'Several'),
    ('More than half the days', 'More than half the days'),
    ('Nearly every day', 'Nearly every day'),
    ]
a1CHOICES= [
    ('Often', 'Often'),
    ('Most of the times', 'Most of the times'),
    ('Sometimes', 'Sometimes'),
    ('Not at all', 'Not at all'),
    ]

bCHOICES= [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ]

cCHOICES= [
    ('Hardly ever', 'Hardly ever'),
    ('Sometimes', 'Sometimes'),
    ('Often', 'Often'),
    ]
dCHOICES= [
    ('I plan a lot', 'I plan a lot'),
    ('50-50', '50-50'),
    ('I mostly focus on taking action', 'I mostly focus on taking action'),
    ]
eCHOICES= [
    ('Satisfied', 'Satisfied'),
    ('Not So Satisfied', 'Not So Satisfied'),
    ('I cry a bit', 'I cry a bit'),
    ]

fCHOICES= [
    ('Really Difficult', 'Really Difficult'),
    ('Kinda', 'Kinda'),
    ('No', 'No'),
    ]
gCHOICES= [
    ('Yes and yes', 'Yes and yes'),
    ('Yes and no', 'Yes and no'),
    ('No and no', 'No and no'),
    ]


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'



# class UserForm(forms.ModelForm):
#     favorite_fruit= forms.ChoiceField(choices=FCHOICES, widget=forms.RadioSelect())
#     class Meta:
#         fields = ('first_name', 'last_name',)
#         model = Order()


class BlogCommentsForm(forms.ModelForm):
    f1 = forms.ChoiceField(choices=FCHOICES, widget=forms.RadioSelect())
    f2 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f3 = forms.ChoiceField(choices=a1CHOICES, widget=forms.RadioSelect())
    f4 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f5 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f6 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f7 = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    f8 = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    f9 = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    f10 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f11 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f12 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f13 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f14 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f15 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f16 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f17 = forms.ChoiceField(choices=eCHOICES, widget=forms.RadioSelect())
    f18 = forms.ChoiceField(choices=dCHOICES, widget=forms.RadioSelect())
    f19 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f20 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f21 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f22 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    f23 = forms.ChoiceField(choices=eCHOICES, widget=forms.RadioSelect())
    f24 = forms.ChoiceField(choices=fCHOICES, widget=forms.RadioSelect())
    f25 = forms.ChoiceField(choices=gCHOICES, widget=forms.RadioSelect())
    f26 = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    f27 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    class Meta:
        model= BlogComments
        fields= '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['f1'].label = 'How creative would you call yourself ?'
        self.fields['f2'].label = 'Do you have any hobbies?'
        self.fields['f3'].label = 'Do you often find yourself in a rut(habit or pattern of behavior that has become dull and unproductive but is hard to change)?'
        self.fields['f4'].label = 'Do you get interested in doing something new everyday?'
        self.fields['f5'].label = 'Do you have little interest or pleasure in doing things?'
        self.fields['f6'].label = 'Have you ever thoughts that you would be better off dead, or of hurting yourself?'
        self.fields['f7'].label = 'Do you feel lonely and isolated due to lack of family unity?'
        self.fields['f8'].label = 'Is family relation less important to people close to you?'
        self.fields['f9'].label = "Do you feel like you can't focus on doing things and have an unstable mind?"
        self.fields['f10'].label = 'Do you feel of giving up and leave everything?'
        self.fields['f11'].label = 'Do you feel bad about yourself or that you are a failure or have let yourself or your family down?'
        self.fields['f12'].label = 'Do you feel like you do not care about anything anymore? '
        self.fields['f13'].label = 'Many times have complains of aches, pains and feeling tired?'
        self.fields['f14'].label = 'Ever felt irritable/grouchy/moody most days?'
        self.fields['f15'].label = 'Do you feeling down, depressed, or hopeless?'
        self.fields['f16'].label = 'Do you have trouble falling or staying asleep, or sleeping too much?'
        self.fields['f17'].label = 'How do you feel when you go to bed?'
        self.fields['f18'].label = 'Do you spend more time planning the day or in taking action? '
        self.fields['f19'].label = 'Do you get interested in trying a new hobby?'
        self.fields['f20'].label = 'Do you feeling tired or having little energy?'
        self.fields['f21'].label = 'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual?'
        self.fields['f22'].label = 'Do you have poor appetite or overeating?'
        self.fields['f23'].label = 'Are you satisfied with your current job or education?'
        self.fields['f24'].label = 'Do you find it difficult to concentrate on this job/education?'
        self.fields['f25'].label = 'Do you have a dream? Is your current status anywhere near it?'
        self.fields['f26'].label = 'Are you satisfied with the amount of effort you put in to achieve your dream?'
        self.fields['f27'].label = 'Do you feel trouble concentrating on things, such as reading the newspaper or watching television?'
