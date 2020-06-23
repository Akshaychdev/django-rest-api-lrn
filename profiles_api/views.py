from rest_framework.views import APIView # REST API Views(Django REST framework)
# All API views expected to return a std. Response
from rest_framework.response import Response
# Status object contains handy HTTP status codes, one can use when returning responses
from rest_framework import status
# Importing viewsets
from rest_framework import viewsets

from . import serializers
