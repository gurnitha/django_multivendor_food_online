# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth import logout

# Locals
from app.accounts.forms import UserRegistrationForm
from app.accounts.models import CustomUser, UserProfile
from app.vendors.forms import VendorRegistrationForm

# Create your views here.

# User: register
def registeruser(request):
	# Handling the loggeg in user
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:dashboard')

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
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:dashboard')
		
	# Check if the request is POST
	if request.method == 'POST':
		# Store the data and create user
		ureg_form = UserRegistrationForm(request.POST)
		vreg_form = VendorRegistrationForm(request.POST, request.FILES)
		# Check if form is valid
		if ureg_form.is_valid() and vreg_form.is_valid():
			first_name = ureg_form.cleaned_data['first_name']
			last_name = ureg_form.cleaned_data['last_name']
			username = ureg_form.cleaned_data['username']
			email = ureg_form.cleaned_data['email']
			password = ureg_form.cleaned_data['password']
			user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
			user.role = CustomUser.VENDOR
			user.save()
			# Do not save this user to vreg_form
			vendor = vreg_form.save(commit=False)
			vendor.user = user 
			# Get user profile from CustomUser which defined in signals
			user_profile = UserProfile.objects.get(user=user)
			vendor.user_profile = user_profile
			vendor.save()
			messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
			return redirect('accounts:registervendor')
		else:
			print('invalid ureg_form and vreg_form')
			print(ureg_form.errors)
			print(vreg_form.errors)
	else:
		ureg_form = UserRegistrationForm()
		vreg_form = VendorRegistrationForm()

	context = {
		'ureg_form': ureg_form,
		'vreg_form': vreg_form
	}
	return render(request, 'app/accounts/registerVendor.html', context)

# User or Vendor: Login
def login(request):
	# Handling the loggeg in user
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:dashboard')

	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(email=email, password=password)
		# If user exist
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You are now logged in.')
			return redirect('accounts:dashboard')
		# If user is not exist
		else: 
			messages.error(request, 'Invalid login credentials')
			return redirect('accounts:login')

	return render(request, 'app/accounts/login.html')


# Logout: Customer or Vendor
def logout(request):
	auth.logout(request)
	messages.info(request, 'You are logged out. Login again?')
	return redirect('accounts:login')

def dashboard(request):
	return render(request, 'app/accounts/dashboard.html')