from django.shortcuts import render, redirect
from .models import WebAccountManager
from .forms import WebAccountManagerForm
from django.contrib.auth import authenticate
from util.text_local import sendSMS
from django.contrib import messages
# Create your views here.


def dashboard(request):

	password_list = WebAccountManager.objects.filter(owner = request.user)
	password_form = WebAccountManagerForm(request.POST or None)

	if request.method == "POST":
		if password_form.is_valid():
			instance = password_form.save(commit = False)
			instance.owner = request.user
			instance.save()
			return redirect("webaccountmanager:dashboard")
		else:
			#Validation Code
			pass
	else:
		password_form = WebAccountManagerForm()

	context = {
		"password_form":password_form,
		"password_list":password_list
	}

	return render(request, "webaccountmanager/dashboard.html", context)

def delete_account(request, account_id):

	if account_id:
		passwordmanager = WebAccountManager.objects.get(id = account_id)

		if passwordmanager:
			passwordmanager.delete()
			return redirect("webaccountmanager:dashboard")
	else:
		#Validation for accoutn_id not present
		pass

def update_account(request, account_id):

	password_list = WebAccountManager.objects.filter(owner = request.user)
	
	if account_id:
		account  = WebAccountManager.objects.get(id = account_id)
		password_form = WebAccountManagerForm(request.POST or None, instance = account)

		if request.method == "POST":
			if password_form.is_valid():
				instance = password_form.save(commit = False)
				instance.save()
				return redirect("webaccountmanager:dashboard")
			else:
				#Validation error
				pass
		
		context = {
			"password_form":password_form,
			"password_list":password_list
		}			
	return render(request, "webaccountmanager/dashboard.html", context)

def view_account(request, account_id):
	if account_id:
		account = WebAccountManager.objects.get(id = account_id, owner = request.user)
		if account:
			context = {
				"account": account
			}
			return render(request,"webaccountmanager/account_detail.html", context)


def send_password(request):
	user = request.user
	password = request.POST["password"]
	user = authenticate(request, username=user.username, password=password)
	mobile = '9970109863'

	if user is not None:
		account_id = request.POST["account_id"] or 0

		if account_id:
			password_obj = WebAccountManager.objects.get(id = account_id)

			if password_obj:
				resp =  sendSMS(mobile,'', 'Your account password '+password_obj.password)
				print(resp)
				messages.error(request, 'Your account password sent on '+mobile)
				return redirect("webaccountmanager:dashboard")
	else:
		messages.info(request, 'Enter correct credentilas.')
		return redirect("webaccountmanager:dashboard")