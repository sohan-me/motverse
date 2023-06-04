from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Teams(models.Model):

	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	designation = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	facebook_link = models.URLField(max_length=200)
	twitter_link = models.URLField(max_length=200)
	google_link = models.URLField(max_length=200)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name
	def get_full_name(self):
		return self.first_name + ' ' + self.last_name
	def team_thumb(self):
		return mark_safe('<img src="%s" width="40" height="40" style="border-radius:50px;"/>' % (self.photo.url))
	team_thumb.short_description = 'Image'

	class Meta:
		verbose_name_plural = 'Teams'