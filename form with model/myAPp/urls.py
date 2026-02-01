from django.urls import path

from myAPp.views import Home, Register

urlpatterns = [
    path('', Home, name="home"),
    path('register/', Register, name="register"),
]