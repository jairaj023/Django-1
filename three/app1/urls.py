from django.urls import path

from app1.views import home, about, login

urlpatterns = [
    path("", home, name="Home Page"),
    path("about/", about, name="About Page"),
    path("demo/login/", login, name="Login Page")
]