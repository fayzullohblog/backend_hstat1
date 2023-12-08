
from .models import MyUser

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ['phone_number', 'user_number_litter', 'role_user', 'state']

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['phone_number', 'user_number_litter', 'role_user', 'state']
