# app.accounts/models.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Locals
from app.accounts.models import CustomUser, UserProfile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)





