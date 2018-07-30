from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Youtube(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	url = models.CharField(max_length = 1000)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	is_downloaded = models.BooleanField(default= False)

	def __str__(self):
		return self.name