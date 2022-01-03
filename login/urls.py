from django.contrib import admin
from django.urls import path, include
import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, names='signup'),
    path('signin', views.signin, names='signin'),
    path('signout', views.signup, names='signup'),
]
