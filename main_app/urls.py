from django.urls import path
from . import views
from .views import Signup

urlpatterns = [
  path('accounts/signup/', Signup.as_view(), name='signup'),   
]