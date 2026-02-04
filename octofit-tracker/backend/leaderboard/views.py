from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Leaderboard
from .serializers import LeaderboardSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [AllowAny]
