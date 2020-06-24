from django.urls import path, include
from feed_api import views
# To link the viewset url - need router class from django rest_framework
from rest_framework.routers import DefaultRouter

app_name = 'feed_api'
router = DefaultRouter()
router.register('', views.UserProfileFeedViewSet)

urlpatterns = [
    # adding router, it generates a list of urls associated with the viewsets
    path('', include(router.urls)),
]
