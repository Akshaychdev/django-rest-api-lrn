from django.shortcuts import render

# REST API Views(Django REST framework)
from rest_framework.views import APIView
# All API views expected to return a std. Response
from rest_framework.response import Response
# Status object contains handy HTTP status codes, one can use when returning responses
from rest_framework import status
from . import serializers

class HelloApiView(APIView):
    """
    API View, to test the functionality
    """
    # This configures the APIView to get the created serializer class, i.e.
    # Whenever sending a 'post'/'patch' request, the expected input is a name
    # with 10 chara. max.(validates)
    serializer_class = serializers.HelloSerializer

    # request = contains request that is made through http-API, format = format
    # suffix for the end of endpoint url(in which format o/p needed-JSON, XML)
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # Endpoint set to - Define a list(here for eg.describes all the features of the API view)
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over application logic',
            'Is mapped manually to URLs',
        ]
        # Every APIView (HTTP) functions described must return a response
        # Response need a Dictionary/List (which will o/p as JSON, when API called)
        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    # Creating the post request
    def post(self, request):
        """Create a hello message with our name"""
        # Retrive the serializer and pass in the data, the 'post' data can
        # be retrived through 'request.data', serializer's Job is to take,
        # validate & convert the data into python object
        serializer = self.serializer_class(data=request.data)
        # validating using the name field received
        if serializer.is_valid():
            # serializer.validated_data must be a dictionary
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else:
            # When the 'post' input data is not valid, need to return'serializer.errors', a
            # dictionary of all the errors based on the validation
            # also need to change (rest_fr status) to 400 bad request(insted of http 200 ok)
            # to inform the API user made a bad request
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    # The return responses(endpoints) only for testing the working
    # Creating a put request
    def put(self, request, pk=None):
        """Handle updating an object"""
        # HTTP Put will update the entire object with what you provided, it will usually
        # done to a specific url primary key
        return Response({"method":"PUT"})

    # HTTP 'Patch',
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        # patch will only update those fiels that are provided in the request
        return Response({"method":"PATCH"})

    # Delete request
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method":"Delete"})
