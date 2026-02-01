from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_home(req):
    return HttpResponse("This is home page")

def app2_about(req):
    return HttpResponse("This is about page")
