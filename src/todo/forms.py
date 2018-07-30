from django import forms
from .models import Project, CommonToDo, ProjectToDo

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ["owner"]
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control col-lg-6'}),
			'description': forms.Textarea(attrs={'class':'materialize-textarea'}),
		}

class ProjectTodoForm(forms.ModelForm):
	class Meta:
		model = ProjectToDo
		exclude = ["project", 'author']
		widgets = {
			'description': forms.Textarea(attrs={'class':'materialize-textarea'}),
		}


class CommonTodoForm(forms.ModelForm):
	class Meta:
		model = CommonToDo
		exclude = ["author"]

		widgets = {
			'description': forms.Textarea(attrs={'class':'materialize-textarea'}),
		}