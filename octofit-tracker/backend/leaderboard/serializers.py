from rest_framework import serializers
from .models import Leaderboard


class LeaderboardSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_name', 'team', 'team_name', 'total_calories', 
                  'total_duration', 'total_activities', 'rank', 'period', 'created_at', 'updated_at']
