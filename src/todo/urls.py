from django.conf.urls import url
from .views import dashboard, project, project_todo, common_todo, change_common_todo_status, change_project_todo_status, update_project, delete_common_todo, delete_project_todo


urlpatterns = [
	url(r'^$', dashboard, name = 'dashboard'),
	url(r'^add_project/', project, name = 'project'),
	url(r'^update_project/(?P<project_id>\d+)/$', update_project, name = 'update_project'),
	url(r'^project_todo/(?P<project_id>\d+)/$', project_todo, name = 'project_todo'),
	url(r'^delete_project_todo/(?P<project_id>\d+)/(?P<todo_id>\d+)/(?P<redirect_to>\w+)/$', delete_project_todo, name = 'delete_project_todo'),

	url(r'^change_project_todo_status/(?P<project_id>\d+)/(?P<todo_id>\d+)/(?P<redirect_to>\w+)/$', change_project_todo_status, name = 'change_project_todo_status'),
	url(r'^common_todo/', common_todo, name = 'todo'),
	url(r'^delete_common_todo/(?P<todo_id>\d+)/(?P<redirect_to>\w+)/$', delete_common_todo, name = 'delete_todo'),
	url(r'^change_common_todo_status/(?P<todo_id>\d+)/(?P<redirect_to>\w+)/$', change_common_todo_status, name = 'change_common_todo_status')
]