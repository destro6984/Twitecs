from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from Users.models import CustomUser


class Tweet(models.Model):
    content = models.CharField(max_length=285)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str_(self):
        return f"content: {self.content}, created: {self.created}, user:{self.user}"
