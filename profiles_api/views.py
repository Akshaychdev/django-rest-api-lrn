from rest_framework import viewsets # Importing viewsets
# from rest_framework.views import APIView # REST API Views(Django REST framework)
# # All API views expected to return a std. Response
# from rest_framework.response import Response
# # Status object contains handy HTTP status codes, one can use when returning responses
# from rest_framework import status
# To authenticate users with the API,
from rest_framework.authentication import TokenAuthentication
# obtain auth token, to get the auth token
from rest_framework.authtoken.views import ObtainAuthToken
# To add search functionality
from rest_framework import filters
# needed the default renderer_classes from api_settings
from rest_framework.settings import api_settings

from . import serializers
from profiles_api import models
from profiles_api import permissions

# 'ModelViewSet' is similer analogy, that creates API viewsets from the existing
# Models
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handle Creating and updating profiles
    """
    serializer_class = serializers.UserProfileSerializer
    # queryset adds which objects in the DB are gonna managed through this viewset
    queryset = models.UserProfile.objects.all()
    # 'TokenAuthentication' works by generating a random token string
    # when the user logs in, then for every requests add this token string to it
    # That act as a password to check that every requesty is authenticated
    # More than one authentication can be applied to a single viewset, just add
    # all the authentication classes to 'authentication_classes'-classs variable
    authentication_classes = (TokenAuthentication,) # To create as Tuple
    # Permission classes(how the user gets permission to do certain things)
    permission_classes = (permissions.UpdateOwnProfile,)
    # The rest_framework comes out of the box with some filters that can be added
    # filtering any viewsets, (one or more filters can be added)
    filter_backends = (filters.SearchFilter,)
    # To tell the filtes which fields needs to be searched
    search_fields = ('name', 'email',)


# Adding login functionality to the API equipped with 'TokenAuthentication'
# 'ObtainAuthToken' can be added directly to urls.py, but it is not enabled as
# default in django admin GUI, need to override-to test easily
class UserLoginApiView(ObtainAuthToken):
    """Handle Creating user authentication Tokens"""
    # obtain the default renderer classes
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # Adds the renderer_classes to ObtainAuthToken view so that it can bee seen
    # in browsable API
