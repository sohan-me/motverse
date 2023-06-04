from django.shortcuts import render, redirect
from .models import Teams
from cars.models import Cars
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	teams = Teams.objects.all()
	featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
	latest_cars = Cars.objects.order_by('created_date').all()
	
	model_search = Cars.objects.values_list('model', flat=True).distinct()
	city_search = Cars.objects.values_list('city', flat=True).distinct()
	year_search = Cars.objects.values_list('year', flat=True).distinct()
	body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()

	
	context = {
	
		'teams' : teams,
		'featured_cars' : featured_cars,
		'latest_cars' : latest_cars,
		'model_search' : model_search,
		'city_search' : city_search,
		'year_search' : year_search,
		'body_style_search' : body_style_search,		
	}
	return render(request, 'tabs/home.html', context)

def about(request):
	teams = Teams.objects.all()
	context = {
		'teams' : teams,
	}
	return render(request, 'tabs/about.html', context)

def services(request):
	return render(request, 'tabs/services.html')

def contact(request):

	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		email_subject = f'You have a new message from motoverse regarding {subject}'
		message_body = f'Name: {name}, Email: {email}, Phone: {phone}, Message: {message}'
		admin_info = User.objects.get(is_superuser=True)

		send_mail(
				    email_subject,
				    message_body,
				    "testcase.noob@gmail.com",
				    [admin_info.email],
				    fail_silently=False,
				)
		messages.success(request, 'Thanks for contacting with us. We will get back to you shortly.')
		return redirect('tabs:contact')

	return render(request, 'tabs/contact.html')