from django.db import models

class Leaderboard(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_calories = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0, help_text='Total duration in minutes')
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    period = models.CharField(max_length=50, default='all_time', help_text='weekly, monthly, all_time')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']
        unique_together = ['user', 'period']

    def __str__(self):
        return f"{self.user.name} - {self.total_calories} calories ({self.period})"
