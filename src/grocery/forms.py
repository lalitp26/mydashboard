from django import forms
from .models import Grocery, GroceryList

class GroceryForm(forms.ModelForm):
	class Meta:
		model = Grocery
		exclude = ["owner"]
		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control col-lg-6'}),
			'total_amount' : forms.TextInput(attrs={'id':'disabled', "disabled":"disabled"})
		}

class GroceryItemForm(forms.ModelForm):
	class Meta:
		model = GroceryList
		exclude = ["grocery"]
		widgets = {
			'description': forms.Textarea(attrs={'class':'materialize-textarea'})
		}