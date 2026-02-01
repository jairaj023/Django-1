from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_login(req):
    return HttpResponse("This is login page")

def app1_register(req):
    email = "info@gmail.com"

    x = 100
    y = 400

    sum = x + y
    return HttpResponse(f"This is register page Your email : {email} total : {sum}")
