from django.contrib import admin
from .models import Contact
# Register your models here.

class AdminContact(admin.ModelAdmin):
	
	list_display = ['id' ,'user_id','first_name', 'last_name', 'car_id', 'inquiry', 'email', 'created_date']
	search_fields = ['email', 'car_id', 'user_id']
	list_filter = ['car_id', 'user_id']
	list_per_page = 25

admin.site.register(Contact, AdminContact)