from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

# Shared URL's
 path('', views.login_form, name='home'),
path('login/', views.loginView, name='login'),
path('logout/', views.logoutView, name='logout'),
path('regform/', views.register_form, name='regform'),
path('register/', views.registerView, name='register'),

    # Librarian URL's
    path('librarian/', views.librarian, name='librarian'),


    # Publisher URL's
    path('publisher/', views.publisher, name='publisher'),
    path('plistbook/', views.PBookListView.as_view(), name='plistbook'),
    path('uabookform/', views.uabookform, name='uabookform'),
    path('uabook/', views.uabook, name='uabook'),


    # Admin URL's
    path('dashboard/', views.dashboard, name='dashboard'),

    ]