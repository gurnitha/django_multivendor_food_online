# app/accounts/forms.py

# Django modules
from django import forms

# Local
from app.accounts.models import CustomUser

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = [
			'first_name', 'last_name', 
			'username', 'email', 'phone_number', 'password'
		]