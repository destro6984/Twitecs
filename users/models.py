from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)



class ProfileUser(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="profiles", default="default.jpg")
    image_from_cl = CloudinaryField('image')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f" {self.user.username} Profile, First_name: {self.user.first_name}, Last_name: {self.user.last_name}, Location: {self.location}, Birth Date: {self.birth_date}"

    # def save(self,**kwargs):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 200 or img.width > 200:
    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
