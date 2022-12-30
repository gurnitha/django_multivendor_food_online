# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Locals
from app.accounts.forms import UserRegistrationForm
from app.accounts.models import CustomUser

# Create your views here.
def registeruser(request):
	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)
		form = UserRegistrationForm(request.POST)
		# Check if the form is valid
		if form.is_valid():
			# Clean the data
			password = form.cleaned_data['password']
			''' If form is valid, the submited 
			data is ready to be save,
			but do not save it yet.
			Assign the data to the user '''
			user = form.save(commit=False)
			# Store passward in hash format
			user.set_password(password)
			# Add role to the user
			user.role = CustomUser.CUSTOMER
			user.save()
			return redirect(registeruser)

	# if the request is GET
	else:
		form = UserRegistrationForm
	
	context = {
		'form': form,
	}
	
	return render(request, 'accounts/registerUser.html', context)