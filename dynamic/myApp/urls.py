from django.urls import path

from myApp.views import Home, About,Contact

urlpatterns = [
    path('', Home, name="Home Page"),
    path('about/', About, name="About Page"),
    path('contact/', Contact, name="Contact Page")
]