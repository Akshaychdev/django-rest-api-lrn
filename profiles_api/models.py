from django.db import models
# The base classes need to use when customizing or overriding Django User model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Inheriting from default/base manager model that comes with django
from django.contrib.auth.models import BaseUserManager

# creating a UserProfileManager() class, pypi guidlines 2 space between classes
# Custom manager is required cz, default django behaviour changed, ie usname replaced with Email


class UserProfileManager(BaseUserManager):
    """
    Manager for User profiles
    """
    # In the manager, write functions that helps manipilate the objects, if a password not specified, it will be None
    # with django, None password wont works, it needed a hash, so until you set a password, one cannot authenticate the user
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        # Chech if email field is empty or null
        if not email:
            # raise a value error exeption, [std behaviour django expects, can display the error msg]
            raise ValueError("User must have an email address")
        # Normalize the email address,(lowercase the second half of the email), method under BaseUserManager
        email = self.normalize_email(email)
        # Creating user model, the manager creates a new user object with norm. email
        user = self.model(email=email, name=name)

        # uses the inbuilt set_password() function in AbstractBaseUser in the user model, to ensure password is hashed
        user.set_password(password)
        # std practice is to specify the database used, as django can support multiple DBs
        user.save(using=self._db)

        # return the newly created user object
        return user

    # All superusers need password, to create a superuser
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        # Class(self) automatically passed in when a fun. calls
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# customize the django default user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database models for users in the system
    inherited from AbstractBaseUser model
    """
    # Store email and name
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # For the permisssion system, is_active, is_staff, is_superuser are some of the basic attributes of Django User object.
    # if a user profile activated or not, By default-activated, but can deactivate(like in fb)

    is_active = models.BooleanField(default=True)
    # If the user is a staff user(ie got acess to admin stuff..etc), By default no one is a staff
    is_staff = models.BooleanField(default=False)

    # Need to specify a model manager ie gonna used for the objects(models), (created above)

    objects = UserProfileManager()

    # More fields to the class, Need a username field( cz we are overriding the default
    # one, need 'email' use insted of username), changed the username field to email field

    USERNAME_FIELD = 'email'
    # The below field set required by default(other than the username field ['email'], at min. a user needs an email and name)
    REQUIRED_FIELDS = ['name']

    # Functions for django to interact with custom user model

    def get_full_name(self):
        """
        Retrive full name of users
        """
        return self.name

    def get_short_name(self):
        """Retrive Short name of user"""
        # Just to demonstrate, not a real method to get a short name
        return self.name

    # IMP: Every model needs a string representation, thing gonna return when converting user profile object to a string
    def __str__(self):
        """Return String Representation of the user( by email address)"""
        return self.email
