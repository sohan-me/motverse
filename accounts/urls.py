from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('accounts/login', views.LogIn, name='LogIn'),
	path('accounts/signup', views.SignUp, name='SignUp'),
	path('accounts/LogOut', views.LogOut, name='LogOut'),
	path('accounts/dashboard', views.DashBoard, name='DashBoard'),
]