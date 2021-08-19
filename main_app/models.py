from django.db import models
from django.db.models import Model, CharField, OneToOneField
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Profile(Model):
  user = OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
  current_city = CharField(max_length=50)
  profile_img = CharField(max_length=500)

  def __str__(self):
    return self.user, current_city



# class User(AbstractUser):
#   pass
