from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Signup(View):

    def get(self,request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)


    # def post(self,request):
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         # create our user in the database
    #         user = form.save()
    #         login(request, user)
    #         return redirect("artist_list")
    #     else:
    #         context = {"form": form}
    #         return render(request, "registration/signup.html", context)