from django.urls import path
from . import views

from .views import Signup, Home, ProfileDetail, NameProfileEdit, PostDetail, CityProfileEdit, ProfileRedirect, Cities, CityPost, PostEdit, PostDelete


urlpatterns = [
    path('accounts/signup/', Signup.as_view(), name='signup'),
    path('profile/', ProfileRedirect.as_view(), name='profile_redirect'),
    path('', Home.as_view(), name='home.html'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('profile/<int:pk>/name/edit',
         NameProfileEdit.as_view(), name='edit_name'),
    path('profile/<int:pk>/city/edit',
         CityProfileEdit.as_view(), name='edit_city'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', PostEdit.as_view(), name="post_edit"),
    path('post/<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
    path('cities/', Cities.as_view(), name='cities'),
    path('cities/post/', CityPost.as_view(), name='city_post'),
    path('cities/<int:pk>/', Cities.as_view(), name='city_detail'),
]
