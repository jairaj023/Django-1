from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    heading = "<h2>Samyak Classes </h2>"
    # return HttpResponse("Hello world")
    return HttpResponse(heading)


def about(req):
    return HttpResponse("About page")