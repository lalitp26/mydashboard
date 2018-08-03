from django.conf.urls import url
from .views import dashboard, update, delete, details, update_grocery_item, delete_grocery_item

app_name = "grocery"

urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
	url(r'^(?P<grocery_id>\d+)/delete$', delete, name = 'delete'),
	url(r'^(?P<grocery_id>\d+)/update$', update, name = 'update'),
	url(r'^(?P<grocery_id>\d+)/details$', details, name = 'details'),
	url(r'^(?P<grocery_id>\d+)/grocery/(?P<grocery_item_id>\d+)/delete$', delete_grocery_item, name = 'delete_item'),
	url(r'^(?P<grocery_id>\d+)/grocery/(?P<grocery_item_id>\d+)/update$', update_grocery_item, name = 'update_item'),

]