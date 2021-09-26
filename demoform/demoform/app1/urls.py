
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('home', views.home, name="home"),
    path('viewdetails', views.viewdetails, name="viewdetails"),
    path('form1', views.form1, name="form1"),
    path('relative', views.relative, name="relative"),



]