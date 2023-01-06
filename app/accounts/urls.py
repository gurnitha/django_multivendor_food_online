# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views

app_name = 'accounts'

urlpatterns = [

	# Register
	path('registeruser/', views.registeruser, name='registeruser'),    
	path('registervendor/', views.registervendor, name='registervendor'),

	# Login, logout, dashboard
	path('login/', views.login, name='login'),    
	path('logout/', views.logout, name='logout'),    
	path('dashboard/', views.dashboard, name='dashboard'),    
] 
