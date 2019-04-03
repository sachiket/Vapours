
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import RadioSelect
# from .models import Order
from django import forms
from django.contrib.auth.models import User
from .models import Blog

BODY= [
        ('3','Normal weight'),
        ('2','Underweight'),
        ('1','Overweight'),
        ('0','Obese'),
    ]
GENDER= [
    ('1', 'Male'),
    ('0', 'Female'),
    ('3', 'Transgender Male'),
    ('4', 'Transgender Female'),
    ]
SEX= [
    ('1', 'Gay/Lesbian'),
    ('0', 'Bisexul'),
    ('2', 'Strainght'),
    ]
PAY=[
        ('2', 'Yes and I have'),
        ('1', "Yes and I haven't"),
        ('0', 'No'),
    ]

FCHOICES= [
    ('2', 'Low'),
    ('1', 'Moderate'),
    ('0', 'High'),
    ]
aCHOICES= [
    ('0', 'Not at all'),
    ('1', 'Several'),
    ('2', 'More than half the days'),
    ('3', 'Nearly every day'),
    ]
a1CHOICES= [
    ('3', 'Often'),
    ('2', 'Most of the times'),
    ('2', 'Sometimes'),
    ('1', 'Not at all'),
    ]

bCHOICES= [
    ('1', 'Yes'),
    ('5', 'No'),
    ]

b1CHOICES= [
    ('1', 'Yes'),
    ('3', 'No'),
    ]
b2CHOICES= [
    ('0', 'Yes'),
    ('2', 'No'),
    ]
b3CHOICES= [
    ('1', 'Yes'),
    ('0', 'No'),
    ]
cCHOICES= [
    ('1', 'Hardly ever'),
    ('2', 'Sometimes'),
    ('3', 'Often'),
    ]
dCHOICES= [
    ('2', 'I plan a lot'),
    ('1', '50-50'),
    ('0', 'I mostly focus on taking action'),
    ]
eCHOICES= [
    ('0', 'Satisfied'),
    ('1', 'Not So Satisfied'),
    ('2', 'I cry a bit'),
    ]

fCHOICES= [
    ('2', 'Really Difficult'),
    ('1', 'Kinda'),
    ('0', 'No'),
    ]
gCHOICES= [
    ('0', 'Yes and yes'),
    ('2', 'Yes and no'),
    ('3', 'No and no'),
    ]


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'






class BlogCommentsForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    Sexuality = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())
    Body_weight = forms.ChoiceField(choices=BODY, widget=forms.RadioSelect())
    Virgin = forms.ChoiceField(choices=b3CHOICES, widget=forms.RadioSelect())
    Prostitution_legal = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    Pay_for_sex = forms.ChoiceField(choices=PAY, widget=forms.RadioSelect())
    # Friends = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    Social_fear = forms.ChoiceField(choices=b3CHOICES, widget=forms.RadioSelect())
    PHQ1A = forms.ChoiceField(choices=FCHOICES, widget=forms.RadioSelect())
    PHQ1B = forms.ChoiceField(choices=b2CHOICES, widget=forms.RadioSelect())
    PHQ1C = forms.ChoiceField(choices=a1CHOICES, widget=forms.RadioSelect())
    PHQ1D = forms.ChoiceField(choices=b2CHOICES, widget=forms.RadioSelect())
    #f5 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ9  = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ6A = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    PHQ6B = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    PHQ6C = forms.ChoiceField(choices=cCHOICES, widget=forms.RadioSelect())
    PHQ6D = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    #f11 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ2A = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    PHQ2B = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    PHQ2C = forms.ChoiceField(choices=bCHOICES, widget=forms.RadioSelect())
    #f15 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ3 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ4A = forms.ChoiceField(choices=eCHOICES, widget=forms.RadioSelect())
    PHQ4B = forms.ChoiceField(choices=dCHOICES, widget=forms.RadioSelect())
    PHQ4C = forms.ChoiceField(choices=b1CHOICES, widget=forms.RadioSelect())
    #f20 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ8 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ5 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    PHQ7A = forms.ChoiceField(choices=eCHOICES, widget=forms.RadioSelect())
    PHQ7B = forms.ChoiceField(choices=fCHOICES, widget=forms.RadioSelect())
    PHQ7C = forms.ChoiceField(choices=gCHOICES, widget=forms.RadioSelect())
    PHQ7D = forms.ChoiceField(choices=b1CHOICES, widget=forms.RadioSelect())
    #f27 = forms.ChoiceField(choices=aCHOICES, widget=forms.RadioSelect())
    class Meta:
        model= Blog
        fields= '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields['Name'].label = 'Name'
        # self.fields['Age'].label = 'Age'
        # self.fields['Gender'].label = 'Gender'
        # self.fields['Sexuality'].label = 'Sexuality'
        # self.fields['Body_weight'].label = 'Body_weight'
        self.fields['Virgin'].label = 'Virginity'
        self.fields['Prostitution_legal'].label = 'Do you think prostitution is legal?'
        self.fields['Pay_for_sex'].label = 'What are your views on pay for sex?'
        # self.fields['Friends'].label = 'Number of close friends ?'
        self.fields['Social_fear'].label = 'Do you have social fear?'
        self.fields['PHQ1A'].label = 'How creative would you call yourself?'
        self.fields['PHQ1B'].label = 'Do you have any hobbies?'
        self.fields['PHQ1C'].label = 'Do you often find yourself in a rut(habit or pattern of behavior that has become dull and unproductive but is hard to change)?'
        self.fields['PHQ1D'].label = 'Do you get interested in doing something new everyday?'
        #self.fields['f5  '].label = 'Do you have little interest or pleasure in doing things?'
        self.fields['PHQ9'].label = 'Have you ever thoughts that you would be better off dead, or of hurting yourself?'
        self.fields['PHQ6A'].label = 'Do you feel lonely and isolated due to lack of family unity?'
        self.fields['PHQ6B'].label = 'Is family relation less important to people close to you?'
        self.fields['PHQ6C'].label = "Do you feel like you can't focus on doing things and have an unstable mind?"
        self.fields['PHQ6D'].label = 'Do you feel of giving up and leave everything?'
        #self.fields['f11 '].label = 'Do you feel bad about yourself or that you are a failure or have let yourself or your family down?'
        self.fields['PHQ2A'].label = 'Do you feel like you do not care about anything anymore? '
        self.fields['PHQ2B'].label = 'Many times have complains of aches, pains and feeling tired?'
        self.fields['PHQ2C'].label = 'Ever felt irritable/grouchy/moody most days?'
        #self.fields['f15 '].label = 'Do you feeling down, depressed, or hopeless?'
        self.fields['PHQ3'].label = 'Do you have trouble falling or staying asleep, or sleeping too much?'
        self.fields['PHQ4A'].label = 'How do you feel when you go to bed?'
        self.fields['PHQ4B'].label = 'Do you spend more time planning the day or in taking action? '
        self.fields['PHQ4C'].label = 'Do you get interested in trying a new hobby?'
        #self.fields['f20 '].label = 'Do you feeling tired or having little energy?'
        self.fields['PHQ8'].label = 'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual?'
        self.fields['PHQ5'].label = 'Do you have poor appetite or overeating?'
        self.fields['PHQ7A'].label = 'Are you satisfied with your current job or education?'
        self.fields['PHQ7B'].label = 'Do you find it difficult to concentrate on this job/education?'
        self.fields['PHQ7C'].label = 'Do you have a dream? Is your current status anywhere near it?'
        self.fields['PHQ7D'].label = 'Are you satisfied with the amount of effort you put in to achieve your dream?'
        #self.fields['f27'].label = 'Do you feel trouble concentrating on things, such as reading the newspaper or watching television?'
