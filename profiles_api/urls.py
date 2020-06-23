from django.urls import path, include
from profiles_api import views
# To link the viewset url - need router class from django rest_framework
from rest_framework.routers import DefaultRouter

app_name = 'profiles_api'

# Assign router to a variable
router = DefaultRouter()
# First argument is, the name of url(like path, no need '/')
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    # adding router, it generates a list of urls associated with the viewsets
    path('', include(router.urls)),

]
