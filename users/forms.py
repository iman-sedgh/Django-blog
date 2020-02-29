from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    emailADDR = forms.EmailField()
    tarikh = forms.FileField()
    class Meta:
        model = User
        fields = ['username', 'emailADDR', 'email','password1','password2']
