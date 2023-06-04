from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from multiselectfield.utils import get_max_length
from django.utils.html import mark_safe

# Create your models here.

class Cars(models.Model):

	state_choice = (

	('AL', 'Alabama'),
	('AK', 'Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DE', 'Delaware'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI', 'Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('KY', 'Kentucky'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),

	)

	featured_choices = (

	('Cruise Control', 'Cruise Control'),
	('Audio Interface', 'Audio Interface'),
	('Bluetooth Connectivity', 'Bluetooth Connectivity'),
	('Backup Camera', 'Backup Camera'),
	('Navigation System', 'Navigation System'),
	('Keyless Entry', 'Keyless Entry'),
	('Leather Seats', 'Leather Seats'),
	('Heated Seats', 'Heated Seats'),
	('Sunroof/Moonroof', 'Sunroof/Moonroof'),
	('Parking Sensors', 'Parking Sensors'),
	('Emergency Braking', 'Emergency Braking'),
	('Apple CarPlay', 'Apple CarPlay'),
	('Android Auto', 'Android Auto'),
	('Wireless Charging', 'Wireless Charging'),
	('Dual-zone Climate Control', 'Dual-zone Climate Control'),
	('USB Ports', 'USB Ports'),

	)

	door_choices = (

	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),

	)
	
	year_choice = []
	for i in range(2000, (datetime.now().year+1)):
		year_choice.append((i,i))

	car_title = models.CharField(max_length=260)
	state = models.CharField(choices=state_choice, max_length=300)
	city = models.CharField(max_length=300)
	color = models.CharField(max_length=300)
	model = models.CharField(max_length=300)
	year = models.IntegerField(('year'), choices=year_choice)
	condition = models.CharField(max_length=300)
	price = models.IntegerField()
	description = RichTextField()
	car_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	car_image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	car_image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	car_image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	car_image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	features = MultiSelectField(choices=featured_choices, max_length=get_max_length(featured_choices, None)+1,)
	body_style = models.CharField(max_length=300)
	engine = models.CharField(max_length=300)
	transmission = models.CharField(max_length=300)
	interior = models.CharField(max_length=300)
	miles = models.IntegerField()
	doors = models.CharField(max_length=300, choices=door_choices)
	passengers = models.IntegerField()
	vin_no = models.CharField(max_length=300)
	miliage = models.IntegerField()
	fuel_type = models.CharField(max_length=300)
	no_of_owners = models.CharField(max_length=300)
	is_featured = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True, blank=True)

	def car_thumb(self):
		return mark_safe('<img src="%s" width="40" height="40" style="border-radius:50px;"/>' % (self.car_image.url))
	car_thumb.short_description = 'Image'

	def __str__(self):
		return self.car_title

	class Meta():
		verbose_name_plural = 'Cars'