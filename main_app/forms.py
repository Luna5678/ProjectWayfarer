from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Profile, Post


class ProfileForm(UserCreationForm):
    current_city= forms.CharField()
    image = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'current_city', 'image', 'email', 'password1', 'password2')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("city", "title", "author", "content")