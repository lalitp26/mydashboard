from django import forms

from .models import PasswordManager


class PasswordManagerForm(forms.ModelForm):
	class Meta:
		model = PasswordManager
		exclude = ["owner"]

		widgets = {
			"password" : forms.PasswordInput()
		}