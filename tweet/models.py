from django.utils.timezone import timezone
from django.db import models


# Create your models here.
from users.models import MyUser


class Tweet(models.Model):
    content = models.CharField(max_length=285)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str_(self):
        return f"content: {self.content}, created: {self.created}, user:{self.user}"

class Comments(models.Model):
    text_content=models.CharField(max_length=60)
    tweet= models.ForeignKey(Tweet,on_delete=models.CASCADE)
    author= models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_comment = models.DateTimeField(auto_now_add=True,blank=True)
    def __str_(self):
        return f"content: {self.text_content}, tweet: {self.tweet}, author:{self.author}"