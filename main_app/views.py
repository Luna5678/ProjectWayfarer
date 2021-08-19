from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.base import TemplateView
from .models import Profile
# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.all()
        return context


class Signup(View):

    def get(self,request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)


    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # create our user in the database
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)