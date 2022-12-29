# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from app.accounts.forms import UserRegistrationForm

# Create your views here.
def registeruser(request):
	form = UserRegistrationForm
	context = {
		'form': form,
	}
	return render(request, 'accounts/registerUser.html', context)