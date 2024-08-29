from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'manager', 'image')
    search_fields = ('id', 'name', 'manager__id')
    list_filter = ('manager',)

admin.site.register(Project, ProjectAdmin)
