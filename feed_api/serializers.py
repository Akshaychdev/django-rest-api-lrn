from rest_framework import serializers

from feed_api import models


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """
    Serializes ProfileFeedItem model
    """
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # 'id's are created and updated automatically, both 'id' and 'created_on' are read-only
        # The 'user_profile' must be based on the authenticated user who creates the feed
        # So don't need user to manually create a feed item - make the 'user_profile' read only
        # (a security flaw can occur like a user assign the created feed to another user)
        extra_kwargs = {'user_profile': {'read_only': True}}
