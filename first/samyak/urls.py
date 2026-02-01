"""
URL configuration for samyak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from app1 import views
from app2.views import app2_home, app2_about
from app1.views import app1_login, app1_register

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', app2_home, name="Home Page"),
    path('about/', app2_about, name="About Page"),

    path('login/', app1_login, name="Login Page"),
    path('register/', app1_register, name="Register page")
]
