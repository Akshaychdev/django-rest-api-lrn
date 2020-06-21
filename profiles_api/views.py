from django.shortcuts import render

# CBV
from django.views.generic import view
from django.http import HttpResponse

# Create your views here.
class CBView(view):
    """
    CLass based view
    """
    def get(self, request):
        return HttpResponse("Clss pyi")
