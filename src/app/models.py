from app.internal.models.admin_user import AdminUser

from django.db import models



class Person(models.Model):
	name = models.CharField(max_length=255)
	bio = models.TextField(blank=True)
	email = models.EmailField()
	date_of_birth = models.DateField()
	city = models.ForeignKey('app.City', on_delete=models.RESTRICT, related_name='people')
	favorite_places = models.ManyToManyField('app.Place')

	def __str__(self):
		return f'{self.name}'
	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'Person'

class City (models.Model):
	name = models.CharField(max_length=255)
	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'City'
	
class Place (models.Model):
	name = models.CharField(max_length=255)
	class Meta:
		verbose_name = 'Place'
		verbose_name_plural = 'Place'

class For_Bot (models.Model):
	user_id = models.IntegerField()
	name = models.CharField(max_length=70, verbose_name = 'Имя')
	tel = models.CharField (blank=True,max_length=15)
	user_name = models.CharField(max_length=70)
	class Meta:
		verbose_name = 'For_Bot'
		verbose_name_plural = 'For_Bot'


	
