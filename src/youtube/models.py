from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Youtube(models.Model):

	PRIORITY = (
			('H','High'),
			('L','Low'),
			('M','Medium')
		)

	owner = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	url = models.CharField(max_length = 1000)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	priority = models.CharField(max_length=10,choices=PRIORITY, unique=True)
	author = models.CharField(blank = True, max_length = 100)
	total_videos = models.IntegerField(default = 0)
	downloaded_videos = models.IntegerField(default = 0)
	thumbnail_url = models.CharField(blank = True, max_length = 1000)
	# video_quality = 
	is_downloaded = models.BooleanField(default= False)

	def __str__(self):
		return self.name