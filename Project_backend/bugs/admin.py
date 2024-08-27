from django.contrib import admin
from bugs.models import Bug

class BugsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'screenshot_type', 'bug_type', 'assignedproject', 'assigneduser', 'created_at', 'updated_at', 'due_date')
    list_filter = ('bug_type', 'assignedproject', 'assigneduser')
    search_fields = ('title', 'description')

admin.site.register(Bug, BugsAdmin)
