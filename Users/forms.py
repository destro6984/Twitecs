from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Users.models import CustomUser


class UserRegistryForm(UserCreationForm):

    image=forms.ImageField(required=False)
    class Meta:
        model=CustomUser
        fields=["username","password1","password2","email","first_name","last_name","image"]

