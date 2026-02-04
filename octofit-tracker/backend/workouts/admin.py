from django.contrib import admin
from .models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    list_filter = ['difficulty', 'activity_type', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['difficulty', 'title']
