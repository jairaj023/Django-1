from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(req):
    return HttpResponse("<h2>This is login page </h2>")

def register(req):
    return HttpResponse("<h2>This is register page</h2>")