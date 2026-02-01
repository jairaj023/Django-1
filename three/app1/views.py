from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(req):
    return HttpResponse("<h1>Home Page </h1>")

def about(req):
    return render(req, "about.html")

def login(req):
    return render(req, "login.html")