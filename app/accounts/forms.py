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
			'username', 'email', 'password'
		]

	def clean(self):
		cleaned_data = super(UserRegistrationForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError(
				"Password does not match!"
		)