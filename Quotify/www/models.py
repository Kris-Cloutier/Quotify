from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=100)
	mobile_number = models.CharField(max_length=100)
	home_number = models.CharField(max_length=100)
	work_number = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	company = models.CharField(max_length=100)
	job_title = models.CharField(max_length=100)
	address = models.CharField(max_length=250)
	notes = models.TextField(max_length=500)

	def __str__(self):
		return self.name