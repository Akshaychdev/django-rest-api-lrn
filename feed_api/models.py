from django.db import models
# Used to retrive settings from settings.py
from django.conf import settings


# Model that stores Status updates in the system
class ProfileFeedItem(models.Model):
    """
    Profile Status Update
    """
    # For every new update, its gonna create a new profile feed item object
    # and associate the object with the user who creates it.
    # The model is linked to "user" model by a foreign key, integrity is
    # maintained (cannot create a feed for non-existant user)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    # When referencing the AUTH usermodel in Django, best practice is to retrive
    # it from settings.py(futureproof any changes), CASCADE: user deleted all fields also deleted
    status_text = models.CharField(max_length=255)
    # Automatically add the date-time when created
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return model as string"""
        return self.status_text
