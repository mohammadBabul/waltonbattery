
from django.contrib import admin
from django.urls import path, include
from battery.views import profile_upload
from battery.views import  home_page

urlpatterns = [
    path('', profile_upload, name="profile_upload"),
    path('home/',  home_page, name="home_page"),
  
]
