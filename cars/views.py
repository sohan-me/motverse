from django.shortcuts import render
from .models import Cars
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def cars(request):
	cars = Cars.objects.all()
	paginator = Paginator(cars, 4)
	paged_cars = paginator.get_page(request.GET.get('page'))

	model_search = Cars.objects.values_list('model', flat=True).distinct()
	city_search = Cars.objects.values_list('city', flat=True).distinct()
	year_search = Cars.objects.values_list('year', flat=True).distinct()
	body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
	
	context = {
		'cars' : paged_cars,
		'model_search' : model_search,
		'city_search' : city_search,
		'year_search' : year_search,
		'body_style_search' : body_style_search,	
	}
	return render(request, 'cars/cars.html', context)


def CarDetails(request, id):
    car_info = Cars.objects.get(id=id)
    car_name = car_info.car_title
    
    context = {
        'car_info': car_info,
        'car_name': car_name,
    }
    return render(request, 'cars/car_details.html', context)



def search(request):

    cars = Cars.objects.order_by('-created_date')
    print(request.GET)

    keyword = request.GET.get('keyword')
    if keyword:
        cars = cars.filter(Q(description__icontains=keyword) | Q(car_title__icontains=keyword))

    model = request.GET.get('model')
    if model:
        cars = cars.filter(model__iexact=model)

    body_style = request.GET.get('body_style')
    if body_style:
        cars = cars.filter(body_style__iexact=body_style)

    city = request.GET.get('city')
    if city:
        cars = cars.filter(city__iexact=city)

    year = request.GET.get('year')
    if year:
        cars = cars.filter(year__iexact=year)

    transmission = request.GET.get('transmission')
    if transmission:
    	cars = cars.filter(transmission__iexact=transmission)

    	
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        cars = cars.filter(price__range=(min_price, max_price))

    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Cars.objects.values_list('transmission', flat=True).distinct()
    context = {
        'cars': cars,
        'model_search' : model_search,
		'city_search' : city_search,
		'year_search' : year_search,
		'body_style_search' : body_style_search,
		'transmission_search' : transmission_search,
    }
    return render(request, 'cars/search.html', context)

