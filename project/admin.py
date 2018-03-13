from django.contrib import admin
from project.models import Project


# Register your models here.

class ProjectModelAdmin(admin.ModelAdmin):
  list_display=['idn']
admin.site.register(Project,ProjectModelAdmin)
