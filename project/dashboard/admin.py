# dashboard/admin.py

from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_assigned', 'due_date', 'priority', 'status')
    list_filter = ('status', 'priority', 'class_assigned')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'