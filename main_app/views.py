# from django.core.checks.messages import Error
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.forms import ModelForm
from .forms import ProfileForm, PostForm
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Profile, User, Post, City
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.edit import UpdateView, CreateView
from django.contrib import messages


# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


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
                return render(request, "home.html", {'form': form})
        else:
            form = ProfileForm()
        return render(request, 'home.html', {'form': form})


# GET
@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

class NameProfileEdit(UpdateView):
    model = User
    fields = [ "first_name","last_name" ]
    template_name = "profile_edit.html"
    

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})
    
class CityProfileEdit(UpdateView):
    model = Profile
    fields = [ "current_city" ]
    template_name = "city_profile_edit.html"
    
    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})
    
class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class ProfileRedirect(View):
    def get(self, request):
        return redirect(f'/profile/{request.user.profile.pk}')

class Cities(TemplateView):
    model = City
    # model = Post
    template_name = "cities.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["posts"] = Post.objects.all()
        context["cities"] = City.objects.all()
        return context

class CitiesPost(TemplateView):
    model = Post
    template_name = "cities.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        # context["cities"] = City.objects.all()
        return context

# class CityPost(CreateView):
#     model = Post
#     fields = ["city", "title", "author", "content"]
#     template_name = "city_post.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(CityPost, self).form_valid(form)

#     def get_success_url(self):
#         # return reverse("cities", kwargs = {"pk": self.object.pk})
#         return reverse("cities")

class CityPost(View):
    def get(self, request):
        form = PostForm()
        context = {
            "form": form}
        return render(request, "city_post.html", context)

    def post(self, request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                post.city = form.cleaned_data.get(
                    'city')
                post.title = form.cleaned_data.get('title')
                post.author = form.cleaned_data.get('author')
                post.content = form.cleaned_data.get('content')
                post.save()
                return redirect('cities')
            else: 
                return render(request, "city_post.html", {'form': form})

    # def post(self, request):
    #     city = request.POST.get("city")
    #     title = request.POST.get("title")
    #     author = request.POST.get("author")
    #     content = request.POST.get("content")
    #     profile = self.request.user.profile
    #     post_ = Post.objects.create(city=city, title=title, author=author, content=content)

    #     return redirect("cities")