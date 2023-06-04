from django.contrib import admin
from .models import Teams
from django.utils.html import format_html
# Register your models here.

class AdminTeamsView(admin.ModelAdmin):
	
	list_display = ['id', 'team_thumb', 'first_name', 'designation', 'created_date']
	list_display_links = ['id', 'team_thumb', 'first_name']
	search_fields = ['first_name', 'last_name', 'designation']
	list_filter = ['designation']

admin.site.register(Teams, AdminTeamsView)