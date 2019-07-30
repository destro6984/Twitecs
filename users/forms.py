from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import MyUser, ProfileUser

Years= [x for x in range(1940,2021)]


class UserRegistryForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]


class UpdateProfileUser(ModelForm):
    birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=Years))
    class Meta:
        model = ProfileUser
        exclude = ('user',)

class UpdateUser(ModelForm):
    class Meta:
        model = MyUser
        fields=["last_name","first_name","email"]
