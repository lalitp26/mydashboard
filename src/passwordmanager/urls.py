from django.conf.urls import url
from .views import dashboard, delete_account, update_account

app_name = "passmanager"

urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
	url(r'^(?P<account_id>\d+)/delete$', delete_account, name = 'delete'),
	url(r'^(?P<account_id>\d+)/update$', update_account, name = 'update'),
]