# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views

app_name = 'accounts'

urlpatterns = [
	path('registeruser', views.registeruser, name='registeruser'),    
	path('registervendor', views.registervendor, name='registervendor'),    
] 
