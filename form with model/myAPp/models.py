from django.db import models

# Create your models here.
class Register(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    repass = models.CharField(max_length=100)