from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .models import User
from . import models
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.hashers import make_password
from django.contrib import auth,messages
# Create your views here.
def login_form(request):
    return render(request,'login.html')
def loginView(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('admin12')
            else:
                return redirect('client')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('home')
def register_form(request):
	return render(request,'register.html')

def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)
		a = User(username=username, email=email, password=password)
		a.save()
		messages.success(request,'Account created successfully')
		return redirect('home')
	else:
		messages.error(request,'Registration failed,try again later')
		return redirect('regform')
def admin12(request):
	return render(request,'admin.html')
def client(request):
	return render(request,'client.html')




