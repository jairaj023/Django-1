from django.contrib import admin

from myAPp.models import Register

# Register your models here.

class showRegister(admin.ModelAdmin):
    list_display = ["id", "fullname", "email", "password", "repass"]

admin.site.register(Register, showRegister)