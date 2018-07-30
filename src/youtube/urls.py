from django.conf.urls import url
from .views import dashboard, delete_youtube, update_youtube

app_name = "youtube"

urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
	url(r'^(?P<youtube_id>\d+)/delete$', delete_youtube, name = 'delete'),
	url(r'^(?P<youtube_id>\d+)/edit$', update_youtube, name = 'edit'),
]