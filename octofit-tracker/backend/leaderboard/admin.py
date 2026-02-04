from django.contrib import admin
from .models import Leaderboard


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'total_calories', 'total_duration', 'total_activities', 'rank', 'period']
    list_filter = ['period', 'team']
    search_fields = ['user__name', 'user__email', 'team__name']
    ordering = ['-total_calories']
