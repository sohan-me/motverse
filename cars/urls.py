from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
	path('cars/', views.cars, name='cars'),
	path('car/<int:id>', views.CarDetails, name='car_details'),
	path('search/', views.search, name='search'),
]