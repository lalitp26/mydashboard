from django import forms

from .models import WebAccountManager

class WebAccountManagerForm(forms.ModelForm):
	class Meta:
		model = WebAccountManager
		exclude = ["owner"]

		widgets = {
			"password" : forms.PasswordInput()
		}


