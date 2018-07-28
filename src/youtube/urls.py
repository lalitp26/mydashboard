from django.conf.urls import url
from .views import dashboard

app_name = "youtube"

urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
]