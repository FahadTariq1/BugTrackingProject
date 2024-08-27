from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectname', 'description', 'manager', 'image')
    search_fields = ('id', 'projectname', 'manager__id')
    list_filter = ('manager',)

admin.site.register(Project, ProjectAdmin)
