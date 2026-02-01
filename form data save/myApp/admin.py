from django.contrib import admin

from myApp.models import RegisterForm

# Register your models here.
class showRegisterModel(admin.ModelAdmin):
    list_display = ["id", "fullname","email", "password"]

admin.site.register(RegisterForm, showRegisterModel)