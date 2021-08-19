from django.db import models
from django.db.models import Model, CharField, OneToOneField
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(Model):
  user = OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
  current_city = CharField(max_length=50, blank=True)
  profile_img = CharField(max_length=500, blank=True)

  def __str__(self):
    return self.user
  # we define signals so our Profile model will be auto created/updated when we create/update User instances
  # @receiver(post_save, sender=User)
  # def create_user_profile(sender, instance, created, **kwargs):
  #     if created:
  #         Profile.objects.create(user=instance)

  # @receiver(post_save, sender=User)
  # def save_user_profile(sender, instance, **kwargs):
  #     instance.profile.save()

  @receiver(post_save, sender=User)
  def update_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)
      instance.profile.save()

