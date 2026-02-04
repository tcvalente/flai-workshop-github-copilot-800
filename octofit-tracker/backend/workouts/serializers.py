from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title', read_only=True)
    difficulty_level = serializers.CharField(source='difficulty', read_only=True)
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        # Return a placeholder since Workout model doesn't have a user field
        return "System"
    
    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'title', 'description', 'activity_type', 
                  'difficulty', 'difficulty_level', 'duration', 'calories_estimate', 
                  'created_at', 'updated_at']
