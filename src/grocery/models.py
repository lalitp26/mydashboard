from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Grocery(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, blank = True)
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):
		return self.title

class GroceryList(models.Model):

	CURRENCY = (
			('inr','inr'),
			('dollar','dollar')
		)

	grocery = models.ForeignKey(Grocery)
	name = models.CharField(max_length = 200)
	description = models.TextField(blank = True)
	req_quantity = models.DecimalField(max_digits=4, decimal_places=2, default = 1.0)
	currency = models.CharField(max_length=10,choices=CURRENCY, default= 'inr')
	quantity = models.DecimalField(max_digits=4, decimal_places=2, default = 0.0)
	price = models.DecimalField(max_digits=7, decimal_places=2, default = 0.0)
	is_purchased = models.BooleanField(default = False)

	def __str__(self):
		return self.name