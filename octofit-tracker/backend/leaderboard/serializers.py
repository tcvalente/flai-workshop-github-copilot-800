from rest_framework import serializers
from .models import Leaderboard


class LeaderboardSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    team = serializers.CharField(source='team.name', read_only=True)
    total_points = serializers.IntegerField(source='total_calories', read_only=True)
    last_updated = serializers.DateTimeField(source='updated_at', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'total_points', 'last_updated', 'total_calories', 
                  'total_duration', 'total_activities', 'rank', 'period', 'created_at', 'updated_at']
