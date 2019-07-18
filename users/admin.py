from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from users.models import ProfileUser, MyUser

admin.site.register(ProfileUser)
admin.site.register(MyUser)