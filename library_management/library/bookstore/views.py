from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .models import User,Book
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


# Shared Views
def login_form(request):
	return render(request, 'bookstore/login.html')

def logoutView(request):
	logout(request)
	return redirect('home')
def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			elif user.is_librarian:
				return redirect('librarian')
			else:
			    return redirect('publisher')
		else:
		    messages.info(request, "Invalid username or password")
		    return redirect('home')


def register_form(request):
	return render(request,'bookstore/register.html')

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




# Publisher views
def publisher(request):
	return render(request, 'publisher/book_list.html')

def uabookform(request):
	return render(request,'publisher/add_book.html')


class PBookListView(ListView):
	model = Book
	template_name = "publisher/book_list.html"
	context_object_name = 'books'
	Paginate_by = 4
	def get_queryset(self):
		return Book.objects.order_by('-id')



def uabook(request):
	if request.method == "POST":
		title = request.POST["title"]
		author = request.POST["author"]
		year = request.POST["year"]
		publisher = request.POST["publisher"]
		desc = request.POST["desc"]


		pdf = request.FILES['pdf']
		cover = request.FILES['cover']
		current_user = request.user
		username = current_user.username
		user_id = current_user.id
		a = Book(title=title, author=author, year=year, publisher=publisher, desc=desc, cover=cover, pdf=pdf, uploaded_by=username,user_id=user_id)
		a.save()

		messages.success(request, 'Book has been uploaded successfully')
		return redirect('publisher')
	else:
		messages.error(request,'Book has not uploaded')
		return redirect('uabookform')







# Librarian views
def librarian(request):
	return render(request, 'librarian/home.html')

# Admin views
def dashboard(request):
	return render(request, 'dashboard/home.html')

