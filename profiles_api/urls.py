from django.urls import path, include
from profiles_api import views
# To link the viewset url - need router class from django rest_framework
from rest_framework.routers import DefaultRouter

app_name = 'profiles_api'

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
# Only provide 'base_name' if you wanna overwrite the base name set Default
# By the 'queryset' name

urlpatterns = [
    # Enabling login Endpoint.
    path('login/', views.UserLoginApiView.as_view()),
    # adding router, it generates a list of urls associated with the viewsets
    path('', include(router.urls)),
]
