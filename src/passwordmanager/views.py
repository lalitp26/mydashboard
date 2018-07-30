from django.shortcuts import render, redirect
from .models import PasswordManager
from .forms import PasswordManagerForm
# Create your views here.


def dashboard(request):

	password_list = PasswordManager.objects.filter(owner = request.user)
	password_form = PasswordManagerForm(request.POST or None)

	if request.method == "POST":
		if password_form.is_valid():
			instance = password_form.save(commit = False)
			instance.owner = request.user
			instance.save()
			return redirect("passmanager:dashboard")
		else:
			#Validation Code
			pass
	else:
		password_form = PasswordManagerForm()

	context = {
		"password_form":password_form,
		"password_list":password_list
	}

	return render(request, "passwordmanager/password_dashboard.html", context)

def delete_account(request, account_id):

	if account_id:
		passwordmanager = PasswordManager.objects.get(id = account_id)

		if passwordmanager:
			passwordmanager.delete()
			return redirect("passmanager:dashboard")
	else:
		#Validation for accoutn_id not present
		pass

def update_account(request, account_id):

	password_list = PasswordManager.objects.filter(owner = request.user)
	
	if account_id:
		account  = PasswordManager.objects.get(id = account_id)
		password_form = PasswordManagerForm(request.POST or None, instance = account)

		if request.method == "POST":
			if password_form.is_valid():
				instance = password_form.save(commit = False)
				instance.save()
				return redirect("passmanager:dashboard")
			else:
				#Validation error
				pass
		
		context = {
			"password_form":password_form,
			"password_list":password_list
		}			
	return render(request, "passwordmanager/password_dashboard.html", context)

			