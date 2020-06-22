from django.shortcuts import render

# REST API Views(Django REST framework)
from rest_framework.views import APIView
# All API views expected to return a std. Response
from rest_framework.response import Response

class HelloApiView(APIView):
    """
    Test API View
    """
    # request = contains request that is made through http-API, format = format
    # suffix foe the end of endpoint url
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # Define a list(here for eg.describes all the features of the API view)
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over application logic',
            'Is mapped manually to URLs',
        ]
        # Every APIView (HTTP) functions described must return a response
        # Response need a Dictionary/List (which will o/p as JSON, when API called)
        return Response({'message':'Hello!', 'an_apiview': an_apiview})
