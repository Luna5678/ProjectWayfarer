from django.urls import path
from . import views
from .views import Signup, Home

urlpatterns = [
  path('accounts/signup/', Signup.as_view(), name='signup'),
  path('', Home.as_view(), name='home'),   
]