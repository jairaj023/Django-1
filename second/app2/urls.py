from django.urls import path

from app2.views import login, register

urlpatterns = [
    path("login/", login, name="Login Page"),
    path("register/", register, name="Register Page"),
]