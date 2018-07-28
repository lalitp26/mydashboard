from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CommonToDo, Project, ProjectToDo
from .forms import ProjectForm, CommonTodoForm, ProjectTodoForm
# Create your views here.


def dashboard(request):
	
	common_todos = CommonToDo.objects.filter(author = request.user)
	projects = Project.objects.filter(owner = request.user)

	context = {
				"common_todo_list":common_todos,
				"projects": projects
	}

	return render(request, 'todo/todo_dashboard.html', context)

def project(request):

	if request.method == "POST":
		project_form = ProjectForm(request.POST)
		if project_form.is_valid():
			instance = project_form.save(commit = False)
			instance.owner = request.user
			instance.save()
			return redirect('/')
	else:
		project_form = ProjectForm()

		projects = Project.objects.filter(owner = request.user)

		context = {
			"projects": projects,
			"project_form":project_form
		}
		return render(request, 'todo/project.html', context)

def update_project(request, project_id):
	if project_id:
		projects = Project.objects.filter(owner = request.user)

		project = Project.objects.get(id = project_id)
		project_form = ProjectForm(request.POST or None, instance = project)
		if request.method == "POST":
			
			if project_form.is_valid():
				instance = project_form.save(commit = False)
				instance.owner = request.user
				instance.save()
				return redirect("project_todo", project_id)

		else:
			context = {
				"projects":projects,
				"project_form":project_form				
			}

			return render(request, 'todo/project.html', context)


def project_todo(request, project_id):
	project = Project.objects.get(id = project_id)
	project_todo_form = ProjectTodoForm(request.POST or None)
	if request.method == "POST":

		if project_todo_form.is_valid():
			instance = project_todo_form.save(commit = False)
			instance.project= project
			instance.author= request.user

			instance.save()

		return redirect("project_todo", project_id=project_id)
	else:
		
		context = {
			"project":project,
			"project_todo_form":project_todo_form
		}

		return render(request, "todo/project_todo.html", context)


def common_todo(request):

	if request.method == "POST":
		common_todo_form = CommonTodoForm(request.POST)
		if common_todo_form.is_valid():
			instance = common_todo_form.save(commit = False)
			instance.author = request.user
			instance.save()
			return redirect('todo')
	else:
		common_todo_form = CommonTodoForm()

		common_todos = CommonToDo.objects.filter(author = request.user)
		
		context = {
			"common_todo_list": common_todos,
			"common_todo_form":common_todo_form}
		
		return render(request, 'todo/common_todo.html', context)

def delete_project_todo(request, project_id, todo_id, redirect_to):

	if todo_id and redirect_to:

		project_todo = ProjectToDo.objects.get(id = todo_id)
		project_todo.delete()

		if redirect_to == "dash":
			return redirect("/")
		else:
			return redirect("project_todo", project_id)

def delete_common_todo(request, todo_id, redirect_to):

	if todo_id and redirect_to:
		todo = CommonToDo.objects.get(id = todo_id)
		todo.delete()

		if redirect_to == "dash":
			return redirect("/")
		else:
			return redirect("todo")


def change_common_todo_status(request, todo_id, redirect_to):
	instance = CommonToDo.objects.get(id = todo_id)
	if instance.is_completed:
		instance.is_completed = False
	else:
		instance.is_completed = True

	instance.save()
	if redirect_to == 'dash':
		return redirect('/')
	else:
		return redirect('todo')

def change_project_todo_status(request, project_id, todo_id, redirect_to):
	if project_id and todo_id:
		project_todo = ProjectToDo.objects.get(id = todo_id)
		is_completed = project_todo.is_completed

		if is_completed:
			project_todo.is_completed = False
		else:
			project_todo.is_completed = True

		project_todo.save()

		if redirect_to == "dash":
			return redirect("/")
		else:
			return redirect("project_todo", project_id)

	else:
		return redirect("/")