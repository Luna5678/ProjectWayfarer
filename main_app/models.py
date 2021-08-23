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
        User, null=False, on_delete=models.CASCADE, related_name="profile")
    current_city = models.CharField(
        max_length=50, blank=False)
    image = models.CharField(
        max_length=500, blank=False)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class City(models.Model):
    city = models.CharField(max_length=60, blank=False)
    country = models.CharField(max_length=60, blank=False) 
    image = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.city
    class Meta:
        ordering = ['city']

class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    content = models.TextField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']



