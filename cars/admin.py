from django.contrib import admin
from .models import Cars
# Register your models here.

class AdminCarView(admin.ModelAdmin):

	list_display = ['id', 'car_thumb', 'car_title', 'color', 'model', 'year', 'condition', 'price', 'engine', 'is_featured']
	search_fields = ['color', 'model', 'condition', 'engine', 'price']
	list_filter = ['color', 'condition']
	list_display_links = ['id', 'car_thumb', 'car_title']
	list_editable = ['is_featured']

admin.site.register(Cars, AdminCarView)