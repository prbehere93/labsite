from django.contrib import admin
from projects.models import Project,Assignment,Comment

# Register your models here.
admin.site.register(Project)
admin.site.register(Assignment)
admin.site.register(Comment)