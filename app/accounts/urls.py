# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views 

urlpatterns = [
	path('registeruser', views.registeruser, name='registeruser'),    
] 
