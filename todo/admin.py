from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = "title", "priority", "date",
    list_filter = "priority", "date",
