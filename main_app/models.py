from django.db import models
from django.db.models import Model, CharField, OneToOneField, DateTimeField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name="profile")
    current_city = models.CharField(
        max_length=50, blank=True)
    image = models.CharField(
        max_length=500, blank=True)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    title = CharField(max_length=60)
    content = TextField(max_length=500)
    created_at = DateTimeField(auto_now_add=True)
    author = CharField(max_length=50)
    # author = ForeignKey(Profile, on_delete=models.CASCADE,
    #                     related_name='profiles')
    location = CharField(max_length=50)
    # location = ForeignKey(
    #     Location, on_delete=models.CASCADE, related_name='locations')

    class Meta:
        ordering = ['created_at']
