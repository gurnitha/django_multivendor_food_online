# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from app.accounts.forms import UserRegistrationForm

# Create your views here.
def registeruser(request):
	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)

	# if the request is GET
	else:
		form = UserRegistrationForm
	
	context = {
		'form': form,
	}
	
	return render(request, 'accounts/registerUser.html', context)