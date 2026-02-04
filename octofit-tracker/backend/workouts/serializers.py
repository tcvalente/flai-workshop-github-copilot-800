from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'activity_type', 'difficulty', 
                  'duration', 'calories_estimate', 'created_at', 'updated_at']
