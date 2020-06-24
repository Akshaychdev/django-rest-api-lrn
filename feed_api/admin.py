from django.contrib import admin

# Register your models here.
from feed_api import models

admin.site.register(models.ProfileFeedItem)
