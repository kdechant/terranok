from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Project

project_extra_fieldsets = ((None, {"fields": ("image", "content", "external_url")}),)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    fieldsets = deepcopy(PageAdmin.fieldsets) + project_extra_fieldsets

admin.site.register(Project, ProjectAdmin)
