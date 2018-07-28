from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	is_active = models.BooleanField(default= False)

	def __str__(self):
		return self.name

class ProjectToDo(models.Model):
	project = models.ForeignKey(Project)
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	is_completed = models.BooleanField(default= False)
	def __str__(self):
		return self.title


class CommonToDo(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	is_completed = models.BooleanField(default= False)

	def __str__(self):
		return self.title