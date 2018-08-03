from django.shortcuts import render, redirect
from todo.models import Project, ProjectToDo, CommonToDo
from webaccountmanager.models import WebAccountManager
from grocery.models import Grocery, GroceryList
from youtube.models import Youtube

from django.http import JsonResponse

from django.db.models import Sum, Count


def login_view(request):
	if request.user.is_authenticated():
		return redirect("dashboard")
	else:
		return render(request, "login.html", {})

def chart_dashboard(request):
	if request.user.is_authenticated():

		projects = Project.objects.filter(owner = request.user)
		common_todos = CommonToDo.objects.filter(author = request.user)
		web_accounts = WebAccountManager.objects.filter(owner = request.user)
		groceries= Grocery.objects.filter(owner = request.user)
		youtube_list = Youtube.objects.filter(owner = request.user)


		total_projects_count = projects.count()
		common_todo_count = common_todos.count()
		web_account_count = web_accounts.count()
		grocery_count = groceries.count()

		context = {
			"youtube_list":youtube_list,
			"projects":projects,
			"common_todo_list":common_todos,
			"web_accounts":web_accounts,
			"total_projects_count":total_projects_count,
			"common_todo_count":common_todo_count,
			"web_account_count":web_account_count,
			"grocery_count":grocery_count
		}
		return render(request, "index.html", context)
	else:
		return redirect('login')
	pass


def chart(request):
	youtube_count = Youtube.objects.filter(owner = request.user).count()
	youtube = Youtube.objects.filter(owner = request.user).values('is_downloaded').annotate(count = Count('is_downloaded'))

	youtube_info = {
		"total_videos":youtube_count,
		"labels":['Not Downloaded', 'Downloaded'],
		"chart_data":[youtube[0]['count'], youtube[1]['count']]
	}
	
	groceries= Grocery.objects.filter(owner = request.user)

	grocery_names_list = []
	grcoery_amount_list = []

	for grocery in groceries:
		grcoery_amount = GroceryList.objects.filter(grocery = grocery).aggregate(total_price = Sum('price'))["total_price"]
		grocery_names_list.append(grocery.title)
		grcoery_amount_list.append(grcoery_amount)

	
	
	
	# project_todos_count = 0

	# for project in projects:
	# 	project_todos_count = project_todos_count+ project.projecttodo_set.all().count()

	context = {
		"youtube_info":youtube_info,
		"grocery": {
			"grocery_names_list":grocery_names_list,
			"grcoery_amount_list":grcoery_amount_list
		}
	}
	return JsonResponse(context)
