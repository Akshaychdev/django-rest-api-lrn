from rest_framework import permissions


# If a user is updating a Status ==> it is in their own profile
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        # Allow 'SAFE_METHODS' && create or retrive own item return True
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
