from django.contrib import admin
from .models import CommonToDo, Project, ProjectToDo

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectToDo)
admin.site.register(CommonToDo)