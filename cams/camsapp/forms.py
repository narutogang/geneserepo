from django import forms
from django.contrib.auth.models import User
from camsapp.models import UserProfileInfo
from django.contrib.auth.forms import AuthenticationForm
#from django.core import validators

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic','member')



#creating single custom validator
##def check_for_z(value):
##    if value[0].lower() !='z':
##        raise forms.ValidationError("name needs to start from z")

#class FormName(forms.Form):
#    name=forms.CharField() #validators=[check_for_z]#)
#    email=forms.EmailField()
#    verify_email =forms.EmailField(label='Enter your email again')
##
#    def clean(self):
        #this is just a single clean method for the entire clean format at once
        #call super -all at once
#        all_clean_data = super().clean()
#        email = all_clean_data['email']
#        vmail = all_clean_data['verify_email']
#        if email != vmail:
#            raise forms.ValidationError("Make sure emails match!")

    #catch bots
        #realistic validator which is built-in
    ##botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
##    validators=[validators.MaxLengthValidator(0)])

    #using default method to create own custom validators
    #it is field inside a class so use self
    #def clean_botcatcher(self):
        ##botcatcher=self.cleaned_data['botcatcher']
        ##if len(botcatcher)>0:
        ##    raise forms.ValidationError("GOTCHA BOT!")
        ##return botcatcher
