from django.urls import path
from . import views as core_views
from .views import Signup, Home
from django.conf.urls import url


urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('accounts/signup/', Signup.as_view(), name='signup'),
]