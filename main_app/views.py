from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm 
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         profile_form = ProfileForm()
#         context = {
#             "form": form,
#             "profile_form": profile_form}
#         return render(request, "registration/signup.html", context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#             profile_form.save()
#             login(request, user)
#             return redirect("/")
#         else:
#             return redirect("signup")

class Signup(View):
    def get(self, request):
        form = ProfileForm()
        context = {
        "form": form}
        return render(request, "registration/signup.html", context)

    def post(self,request):
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.current_city = form.cleaned_data.get('current_city')
                user.profile.image = form.cleaned_data.get('image')
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = ProfileForm()
        return render(request, 'registration/signup.html', {'form': form})


# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username','password','email','first_name', 'last_name')

# class ProfileForm(ModelForm):
#     class Meta:
#         model= Profile
#         fields = ('profile_img', 'current_city')

# class Signup(View):

#     def get(self, request):
#         user_form = UserCreationForm()
#         profile_form = ProfileForm()
#         # user_form = UserForm()
#         context = {"profile_form": profile_form, "user_form": user_form}
#         return render(request, "registration/signup.html", context)


#     def post(self, request):
#         user_form = UserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             # create our user in the database
#             user = user_form.save()
#             profile = profile_form.save()
#             login(request, user, profile)
#             return redirect("/")
#         else:
#             context = {"profile_form": profile_form, "user_form": user_form}
#             return render(request, "registration/signup.html", context)
