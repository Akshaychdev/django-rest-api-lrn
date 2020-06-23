from rest_framework import permissions

# To restrict users modifing profiles other than their own, uses a permissions
# BasePermission helps custom permissions
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    # Add a 'has object permissions' function to the class gets called everytime
    # a request is made(is called as default-can customize it)
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # The rules
        # Need to allow users to view other user's profiles
        # But can make changes only to their own profile
        # SAFE_METHODS = GET..(not any changes made)
        # unsafe methods = PUT, PATCH, DELETE
        if request.method in permissions.SAFE_METHODS:
            return True
        # when a request authenticated, djangoRF will assign the authenticated
        # user profile to the request, can use it to compare with the object that
        # is being updated(make sure they have the same id)
        return obj.id == request.user.id
