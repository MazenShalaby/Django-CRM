from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import TextInput, PasswordInput

from .models import Record

# Create your forms here.


class CreateRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ("first_name", "last_name", 'age', 'phone', 'category', 'tall', 'weight', 'address')

##########################################################################################################

class UpdateRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ("first_name", "last_name", 'age', 'phone', 'category', 'tall', 'weight', 'address')

##########################################################################################################

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2',]

##########################################################################################################

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

