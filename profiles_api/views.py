from rest_framework.views import APIView # REST API Views(Django REST framework)
# All API views expected to return a std. Response
from rest_framework.response import Response
# Status object contains handy HTTP status codes, one can use when returning responses
from rest_framework import status
# Importing viewsets
from rest_framework import viewsets
# To authenticate users with the API,
from rest_framework.authentication import TokenAuthentication

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
