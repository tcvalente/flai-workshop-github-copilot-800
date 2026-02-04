from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Leaderboard
from users.models import User
from teams.models import Team


class LeaderboardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.leaderboard_data = {
            'user': self.user.id,
            'team': self.team.id,
            'total_calories': 1000,
            'total_duration': 120,
            'total_activities': 5,
            'period': 'weekly'
        }
    
    def test_create_leaderboard_entry(self):
        response = self.client.post('/api/leaderboard/', self.leaderboard_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 1)
    
    def test_get_leaderboard(self):
        Leaderboard.objects.create(user=self.user, team=self.team, total_calories=1000, total_duration=120, total_activities=5)
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
