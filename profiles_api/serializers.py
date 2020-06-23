from rest_framework import serializers

from profiles_api import models

# Adding a new serializer for the profiles_api project
# Using a "ModelSerializer", which is similer to a regular serializer
# With some added functionality-easy to work with existing django db models,
# (same functionality like generating forms using ModelForms)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # 'passwords' only needed when creating new users to the system, and users
        # not want to retrive the password hash, so 'password' must be 'write' only
        # So when using 'GET' there won't be any password hash in the request
        # To add this extra-configurations to the already existing DB fields
        extra_kwargs = {
            'password': {
                'write_only': True,
                # custome style, set the input field type to a password field
                'style': {'input_type': 'password'}
            }
        }

    # By default the 'ModelSerializer' allows one to create simple objects in the DB
    # But we got our 'create_user' function on the custom manager(UserProfileManager)
    # So it needs to override the 'create' function using 'create_user' function.
    # cz. of the reason, in 'create_user' fn. password gets created as a "hash",
    # in default it is as clear-text, so under "UserProfileSerializer"

    def create(self, validated_data):
        """Create and return a new user"""
        # The default procedure is, when a new object created using ModelSerializer
        # it validates the data then it call the 'create' function
        # passing in the validated_data, a custom 'create' function which
        # creates and returns a new user from the UserProfile manager
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
