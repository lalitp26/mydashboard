from django import forms
from .models import Youtube


class YoutubeForm(forms.ModelForm):
	class Meta:
		model = Youtube
		exclude = ['owner']

		widgets = {
			'description': forms.Textarea(attrs={'class':'materialize-textarea'})
		}