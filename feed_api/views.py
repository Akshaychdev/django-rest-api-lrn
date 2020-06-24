from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from feed_api import models
from feed_api import permissions


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profile feed items
    """
    # validated, serializer.save() called default
    serializer_class = serializers.ProfileFeedItemSerializer
    # Using Token Authentication
    authentication_classes = (TokenAuthentication,)
    queryset = models.ProfileFeedItem.objects.all()
    # chek out the 79 character limit
    # 'IsAuthenticatedOrReadOnly' from djangoRF, only 'read' if not authenticated
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    # 'perform_create' is built in django method(ModelViewSet), which helps
    # customize the behavior of created objects, called every time for a HTTP 'POST'
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        # When a new object is created, django calles 'perform_create', with the
        # serializer passed as argument, 'self.request.user' :- for every request
        # being made a request object is passed in to all viewsets, the request object
        # contains all information about the request(auth. , http method..etc),
        # if the user is authenticated, it contains a user object too.
        serializer.save(user_profile=self.request.user)
