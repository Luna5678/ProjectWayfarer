from django.db import models
from django.db.models import Model, CharField, OneToOneField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(Model):
  user = OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
  current_city = CharField(max_length=50)
  profile_img = CharField(max_length=500)


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


  def __str__(self):
    return self.user.username



# class User(AbstractUser):
#   pass
