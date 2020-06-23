from rest_framework import serializers

# Serializer is a feature from Django REST Framework, allows one to easily convert data
# Inputs in to python objects (and verify them)
# To add 'post', 'patch', 'update' to the "HelloApiView", then it needs a Serializer
# To receive the contents and verify the request matches..

# Serializer class from module serializers
class HelloSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView
    """
    # Simple serializer - accepts a name input, then adding it to the APIView
    # to test the 'post' functionality

    # Creates a name field(CharField), grab the text like in Django Forms,
    name = serializers.CharField(max_length=10)
