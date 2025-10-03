from django.contrib import admin

# Register your models here.

from .models import Skill, Experience, Project

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)