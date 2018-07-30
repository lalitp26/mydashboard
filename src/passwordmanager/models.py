from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordManager(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	user_name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	account_url = models.CharField(max_length = 500)


	def __str__(self):
		return self.title