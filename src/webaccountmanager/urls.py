from django.conf.urls import url
from .views import dashboard, delete_account, update_account, send_password, view_account

app_name = "webaccountmanager"

urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
	url(r'^send_password/$', send_password, name = 'send_password'),
	url(r'^(?P<account_id>\d+)/delete$', delete_account, name = 'delete'),
	url(r'^(?P<account_id>\d+)/update$', update_account, name = 'update'),
	url(r'^(?P<account_id>\d+)/detail$', view_account, name = 'detail'),
]