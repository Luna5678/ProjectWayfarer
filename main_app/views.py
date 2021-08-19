from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class Signup(View):
    def get(self, request):
        form = ProfileForm()
        context = {
            "form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.current_city = form.cleaned_data.get(
                    'current_city')
                user.profile.image = form.cleaned_data.get('image')
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username,
                                    password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = ProfileForm()
        return render(request, 'registration/signup.html', {'form': form})
