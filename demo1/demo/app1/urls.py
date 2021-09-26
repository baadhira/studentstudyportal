from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URL's
 path('', views.login_form, name='home'),
path('login/', views.loginView, name='login'),
path('regform/', views.register_form, name='regform'),
path('register/', views.registerView, name='register'),
path('admin12/', views.admin12, name='admin12'),
path('client/', views.client, name='client'),
    ]