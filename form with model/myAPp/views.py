from django.shortcuts import render

from myAPp.forms import registerForm

# Create your views here.
def Home(req):
    return render(req, "home.html")


def Register(req):
    form  = registerForm
    return render(req, "register.html", {"form" : form})