# app.accounts/models.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Locals
from app.accounts.models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)





