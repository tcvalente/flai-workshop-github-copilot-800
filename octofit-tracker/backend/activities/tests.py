from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Activity
from users.models import User
from teams.models import Team
from datetime import date


class ActivityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.activity_data = {
            'user': self.user.id,
            'activity_type': 'running',
            'duration': 30,
            'calories': 300,
            'distance': 5.0,
            'date': str(date.today())
        }
    
    def test_create_activity(self):
        response = self.client.post('/api/activities/', self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
    
    def test_get_activities(self):
        Activity.objects.create(user=self.user, activity_type='running', duration=30, calories=300, date=date.today())
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
