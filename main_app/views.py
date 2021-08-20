# from django.core.checks.messages import Error
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.forms import ModelForm
from .forms import ProfileForm
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Profile, User, Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView

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
            form = ProfileForm()
        return render(request, 'registration/signup.html', {'form': form})


# GET
@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # username = self.request.GET.get("username")
        # if username != None:
        # context["profile"] = Profile.objects.filter(
        #     username__icontains=username, user=self.request.user)
        context["posts"] = Post.objects.all()
        return context


class ProfileEdit(UpdateView):
    # form_class = ProfileForm
    # model = Profile
    # template_name = "profile_edit.html"
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileEdit, self).get_context_data(**kwargs)
    #     context['profile'] = Profile.objects.all() #whatever you would like
    #     return context

    # model = User
    # fields = [ "first_name","last_name" ]
    # template_name = "profile_edit.html"

    # model = Profile
    # fields = [ "current_city" ]
    # template_name = "profile_edit.html"

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class ProfileRedirect(View):
    def get(self, request):
        return redirect(f'/profile/{request.user.profile.pk}')