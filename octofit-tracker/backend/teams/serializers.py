from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'member_count', 'created_at', 'updated_at']
    
    def get_member_count(self, obj):
        return obj.members.count()
