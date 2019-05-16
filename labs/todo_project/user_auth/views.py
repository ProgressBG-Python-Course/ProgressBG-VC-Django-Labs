# from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


app_name="create_user"


# login view

# /todos/ => list all tasks
def create_user(request):
	 user = User.objects.create_user('pesho2', 'pesho@peho.com', '123')
	 # we can add/change other properties if we want later

	 user.save();

	 return HttpResponse('user created');

def change_password(request):
	user_name = 'ada'
	new_password = 'addnewpass'

	user = User.objects.get(username=user_name)
	user.set_password(new_password)
	user.save()

	return HttpResponse('user pass changed')

def auth_user(request):
	user = authenticate(username='ada', password='addnewpass')

	if user is not None:
		# the password verified for the user
		if user.is_active:
			return HttpResponse('User is authenticated')		
		else:
			return HttpResponse('account is disabled, the user is valid')
	else:
		# the authentication system was unable to verify the username and password
		return HttpResponse('The username and/or password were incorrect.')

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
		else:
			# Return a 'disabled account' error message
			pass
	else:
		# Return an 'invalid login' error message.
		pass


def logout_view(request):
	logout(request)
	# Redirect to a success page.

@login_required
def restricted_view(request): 
	pass