from django.contrib import admin
from bugs.models import Bug

class BugsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'screenshot_type', 'status', 'assignedproject', 'assigneduser', 'created_at', 'updated_at', 'due_date')
    list_filter = ('status', 'assignedproject', 'assigneduser')
    search_fields = ('title', 'description')

admin.site.register(Bug, BugsAdmin)
