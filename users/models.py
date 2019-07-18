from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)




class ProfileUser(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles", default="default.jpg")

    def __str__(self):
        return f" {self.user.username} Profile"

    def save(self,**kwargs):
        super().save()

        img = Image.open(self.image.path)  # otworzy image obecnej instancji

        if img.height > 300 or img.width > 300:  # warunkujemy image
            output_size = (200, 200)  # max rozmiarów tuple
            img.thumbnail(output_size)  # zmniejsza obraz
            img.save(self.image.path)
