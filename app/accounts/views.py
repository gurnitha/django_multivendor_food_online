# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

# Locals
from app.accounts.forms import UserRegistrationForm
from app.accounts.models import CustomUser
from app.vendors.forms import VendorRegistrationForm

# Create your views here.

# User: register
def registeruser(request):

	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)
		ureg_form = UserRegistrationForm(request.POST)

		# CREATE USER USING THE FORM

		# # Check if the ureg_form is valid
		# if ureg_form.is_valid():
		# 	# Clean the data
		# 	password = ureg_form.cleaned_data['password']
		# 	''' If ureg_form is valid, the submited 
		# 	data is ready to be save,
		# 	but do not save it yet.
		# 	Assign the data to the user '''
		# 	user = ureg_form.save(commit=False)
		# 	# Store passward in hash format
		# 	user.set_password(password)
		# 	# Add role to the user
		# 	user.role = CustomUser.CUSTOMER
		# 	user.save()
		# 	return redirect(registeruser)

		# CREATE USER USING create_user METHOD
		
		if ureg_form.is_valid():
			'''Get the first_name, last_name, username,
			email, password form the create_user method
			and assign the role as CUSTOMER'''
			first_name = ureg_form.cleaned_data['first_name']
			last_name = ureg_form.cleaned_data['last_name']
			username = ureg_form.cleaned_data['username']
			email = ureg_form.cleaned_data['email']
			password = ureg_form.cleaned_data['password']
			user = CustomUser.objects.create_user(
				first_name=first_name, 
				last_name=last_name, 
				username=username, 
				email=email, 
				password=password)
			user.role = CustomUser.CUSTOMER
			user.save()
			messages.success(request, 'Your account has been registered sucessfully!')
			# print('User is created')
			return redirect('accounts:registeruser')

		else:
			print('invalid ureg_form')
			print(ureg_form.errors)


	# if the request is GET
	else:
		ureg_form = UserRegistrationForm
	
	context = {
		'ureg_form': ureg_form,
	}
	
	# return render(request, 'accounts/registerUser.html', context)
	return render(request, 'app/accounts/registerUser.html', context)


# Vendor: register
def registervendor(request):
	ureg_form = UserRegistrationForm # ureg_form is for UserForm in short
	vreg_form = VendorRegistrationForm # vreg_form is for VendorForm in short
	context = {
		'ureg_form': ureg_form,
		'vreg_form': vreg_form
	}
	return render(request, 'app/accounts/registerVendor.html', context)