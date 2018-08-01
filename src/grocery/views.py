from django.shortcuts import render, redirect
from .models import Grocery, GroceryList
from .forms import GroceryForm, GroceryItemForm
# Create your views here.


def dashboard(request):
	grocery_list = Grocery.objects.filter(owner = request.user)
	grocery_form = GroceryForm(request.POST or None)

	if request.method == 'POST':
		if grocery_form.is_valid():
			instance = grocery_form.save(commit = False)
			instance.owner  = request.user

			instance.save()

			return redirect('grocery:dashboard')

	context = {
		"grocery_list": grocery_list,
		"grocery_form":grocery_form
	}

	return render(request, 'grocery/dashboard.html', context)

def update(request, grocery_id):
	grocery_list = Grocery.objects.filter(owner = request.user)
	if grocery_id:

		grocery = Grocery.objects.get(id = grocery_id, owner = request.user)

		if request.method == "POST":
			grocery_form = GroceryForm(request.POST or None, instance = grocery)
			if grocery_form.is_valid():
				instance = grocery_form.save(commit = False)
				instance.save()
				return redirect("grocery:dashboard")
			else:
				return redirect("grocery:dashboard")
				
		else:
			grocery_form = GroceryForm(instance = grocery)
			context = {
				"grocery_list":grocery_list,
				"grocery_form":grocery_form
			}
			return render(request, 'grocery/dashboard.html', context)
			
	else:
		#Grocery id not found error
		return redirect("grocery:dashboard")

def delete(request, grocery_id):

	if grocery_id:
		grocery = Grocery.objects.get(id = grocery_id)
		
		if grocery:
			grocery.delete()
			return redirect("grocery:dashboard")
		else:
			#Grocery not found error
			return redirect("grocery:dashboard")
	else:
		#Grocery id not found error
		return redirect("grocery:dashboard")

def details(request, grocery_id):
	if grocery_id:
		grocery = Grocery.objects.get(id = grocery_id)
		grocery_items_form = GroceryItemForm(request.POST or None)
		
		if grocery:

			if request.method == "POST":
				if grocery_items_form.is_valid():
					instance = grocery_items_form.save(commit = False)
					instance.grocery = grocery
					instance.save()

					return redirect("grocery:details", grocery_id)
			else:
				context = {
					"grocery":grocery,
					"grocery_items_form":grocery_items_form
				}

			return render(request, "grocery/details.html", context)

		else:
			#Grocery not found error
			return redirect("grocery:dashboard")
	else:
		#Grocery id not found error
		return redirect("grocery:dashboard")

def update_grocery_item(request, grocery_id, grocery_item_id):

	if grocery_id and grocery_item_id:
		grocery = Grocery.objects.get(id = grocery_id , owner = request.user)
		grocery_item = GroceryList.objects.get(id = grocery_item_id, grocery= grocery)

		grocery_items_form = GroceryItemForm(request.POST or None, instance = grocery_item)

		if request.method == "POST":
			if grocery_items_form.is_valid():
				instance = grocery_items_form.save(commit = False)
				instance.save()

				return redirect("grocery:details", grocery_id)
			else:
				#Validation error 
				grocery_items_form = GroceryItemForm(instance= grocery_item)

	grocery_items_form = GroceryItemForm(instance= grocery_item)
	context = {
			"grocery":grocery,
			"grocery_items_form":grocery_items_form
		}
	return render(request, "grocery/details.html", context)

def delete_grocery_item(request, grocery_id, grocery_item_id):

	if grocery_id and grocery_item_id:
		grocery = Grocery.objects.get(id = grocery_id, owner = request.user)

		if grocery:
			grocery_item = GroceryList.objects.get(grocery = grocery, id = grocery_item_id)

			if grocery_item:
				grocery_item.delete()
				return redirect("grocery:details", grocery_id)

	else:
		#Error message
		return redirect("grocery:dashboard")
