from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):
    return HttpResponse("The Best Investment we can make is ourself!")
