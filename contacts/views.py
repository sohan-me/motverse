from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from cars.models import Cars
# Create your views here.

def inquiry(request):
	
	car_id = None
	user_id = None
	admin_info = User.objects.get(is_superuser=True)

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		inquiry = request.POST.get('inquiry')
		city = request.POST.get('city')
		state = request.POST.get('state')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		car_title = request.POST.get('car_title')
		car_id = request.POST.get('car_id')
		user_id = request.POST.get('user_id')

		if request.user.is_authenticated:
			has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
			if has_contacted:
				messages.error(request, 'You already made a inquiry for this car. Please wait we get back to you shortly.')
				return redirect(reverse('cars:car_details', args=[car_id]))
			else:
				car = get_object_or_404(Cars, id=car_id)
				contact = Contact(cars=car, first_name=first_name, last_name=last_name, inquiry=inquiry, city=city, state=state, email=email, phone=phone, message=message,
					car_title = car_title, car_id = car_id, user_id = user_id
					)
				contact.save()

				send_mail(
				    "New car inquiry.",
				    f"You have a new inquiry for the car -> {car_title}. Please login to your admin panel for more info.",
				    "testcase.noob@gmail.com",
				    [admin_info.email],
				    fail_silently=False,
				)
				messages.success(request, 'Your inquiry has been submitted. we get back to you shortly.')

		else:
			messages.error(request, 'Please login first before sending any inquiry.')
			return redirect(reverse('cars:car_details', args=[car_id]))
	
	return redirect(reverse('cars:car_details', args=[car_id]))

