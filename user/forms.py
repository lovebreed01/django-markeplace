from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Profile


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=300, help_text='Enter a valid email address ')
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username','email', 'password1','password2']
        help_texts = {
            'phone_number': 'Enter a valid phone number for a complete registration '
        }

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UserUpdateForm(ModelForm): 
    first_name =forms.CharField(max_length=30,required=False) 
    last_name =forms.CharField(max_length=30,required=False) 
    email = forms.EmailField(help_text='Enter a valid email address ')
    class Meta: 
        model = User 
        fields = ['first_name', 'last_name','username','email']

