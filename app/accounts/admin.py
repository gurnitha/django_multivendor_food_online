# app.accounts/models.py

# Django modules
from django.contrib import admin

# Locals
from app.accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)