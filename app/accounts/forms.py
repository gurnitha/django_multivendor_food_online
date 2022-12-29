# app/accounts/forms.py

# Django modules
from django import forms

# Local
from app.accounts.models import CustomUser

class UserRegistrationForm(forms.ModelForm):
	# Membuat field password dan confirm password
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = CustomUser
		fields = [
			'first_name', 'last_name', 
			'username', 'email', 'phone_number', 'password'
		]