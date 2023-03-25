from django.forms import ModelForm
from accounts.models import Account

from django import forms
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name','last_name','selection','region', 'email', 'username']
        
        
from django import forms
from django.contrib.auth.models import User

# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]