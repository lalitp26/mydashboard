from django.shortcuts import render, redirect
from .models import PasswordManager
from .forms import PasswordManagerForm
from django.contrib.auth import authenticate
from util.text_local import sendSMS
from django.contrib import messages
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


def send_password(request):
	user = request.user
	password = request.POST["password"]
	user = authenticate(request, username=user.username, password=password)
	mobile = '9970109863'

	if user is not None:
		account_id = request.POST["account_id"] or 0

		if account_id:
			password_obj = PasswordManager.objects.get(id = account_id)

			if password_obj:
				resp =  sendSMS(mobile,'', 'Your account password '+password_obj.password)
				print(resp)
				messages.error(request, 'Your account password sent on '+mobile)
				return redirect("passmanager:dashboard")
	else:
		messages.info(request, 'Enter correct credentilas.')
		return redirect("passmanager:dashboard")