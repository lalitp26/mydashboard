from django.shortcuts import render, redirect


def login_view(request):
	if request.user.is_authenticated:
		return redirect("dashboard")
	else:
		return render(request, "login.html", {})