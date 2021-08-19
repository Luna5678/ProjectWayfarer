from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username','password','email','first_name', 'last_name')

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields = ('profile_img', 'current_city')

class Signup(View):

    def get(self, request):
        user_form = UserCreationForm()
        profile_form = ProfileForm()
        # user_form = UserForm()
        context = {"profile_form": profile_form, "user_form": user_form}
        return render(request, "registration/signup.html", context)


    def post(self, request):
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # create our user in the database
            user = user_form.save()
            profile = profile_form.save()
            login(request, user, profile)
            return redirect("/")
        else:
            context = {"profile_form": profile_form, "user_form": user_form}
            return render(request, "registration/signup.html", context)