from django.urls import path
from . import views
from .views import Signup, Home, ProfileDetail, NameProfileEdit, PostDetail, CityProfileEdit

urlpatterns = [
    path('accounts/signup/', Signup.as_view(), name='signup'),
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('profile/<int:pk>/name/edit', NameProfileEdit.as_view(), name='edit_name'),
    path('profile/<int:pk>/city/edit', CityProfileEdit.as_view(), name='edit_city'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]
