from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import MyUser


class UserRegistryForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]


