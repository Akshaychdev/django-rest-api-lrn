from django.urls import path, include
from profiles_api import views
# To link the viewset url - need router class from django rest_framework
from rest_framework.routers import DefaultRouter

app_name = 'profiles_api'
