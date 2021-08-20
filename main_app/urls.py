from django.urls import path
from . import views
from .views import Signup, Home, ProfileDetail, ProfileEdit, PostDetail, ProfileRedirect

urlpatterns = [
    path('accounts/signup/', Signup.as_view(), name='signup'),
    path('profile/', ProfileRedirect.as_view(), name='profile_redirect'),
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEdit.as_view(), name='edit'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]
