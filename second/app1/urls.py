from django.urls import path

from app1.views import home, about

urlpatterns = [
    path("", home, name="Home Page"),
    path("about/", about, name="About Page"),
]