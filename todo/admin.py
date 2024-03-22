from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    list_filter = ['title']


admin.site.register(Task, TaskAdmin)