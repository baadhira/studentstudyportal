from django.contrib import admin
from django.conf.urls import url
from library import views
app_name="library"

urlpatterns = [
url(r'^viewdetails/$', views.viewdetails, name="list"),
url(r'^form3/$', views.form3, name="form3"),
url(r'^search/$', views.search, name="search"),
]