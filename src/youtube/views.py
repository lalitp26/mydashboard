from django.shortcuts import render, redirect
from .forms import YoutubeForm
from .models import Youtube

# Create your views here.
def dashboard(request):
	youtube_form = YoutubeForm(request.POST or None)
	youtube_list = Youtube.objects.filter(owner = request.user)

	if request.method == "POST":
		if youtube_form.is_valid():
			instance = youtube_form.save(commit = False)
			instance.owner = request.user
			instance.save()

	context = {
		"youtube_form":youtube_form,
		"youtube_list":youtube_list
	}

	return render(request, "youtube/index.html", context)

def edit_youtube(request, youtube_id):

	youtube_list = Youtube.objects.filter(owner = request.user)

	if youtube_id:
		
		youtube = Youtube.objects.get(id = youtube_id)

		if request.method == "POST":
			youtube_form = YoutubeForm(request.POST or None, instance = youtube)

			if youtube_form.is_valid():
				instance = youtube_form.save(commit = False)
				instance.save()

				return redirect("youtube:dashboard")
			else:
				youtube_form = YoutubeForm()
		else:
				youtube_form = YoutubeForm(instance = youtube)
	else:
		youtube_form = YoutubeForm()

	context = {
		"youtube_form":youtube_form,
		"youtube_list":youtube_list
	}

	return render(request, "youtube/index.html", context)

def delete_youtube(request, youtube_id):
	if youtube_id:
		youtube = Youtube.objects.get(id = youtube_id)

		if youtube:
			youtube.delete()
			return redirect("youtube:dashboard")
		else:
			pass
	else:
		pass