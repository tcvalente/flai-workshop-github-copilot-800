from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'team', 'created_at']
    list_filter = ['team', 'created_at']
    search_fields = ['email', 'name']
    ordering = ['-created_at']
