from django.contrib.auth.models import User
from django.db.models.signals import post_save
from users.models import ProfileUser, MyUser
from django.dispatch import receiver


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance,image_from_cl="image/upload/v1565630684/non_existing_id.png")



@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    instance.profileuser.save(force_insert=False)