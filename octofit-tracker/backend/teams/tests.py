from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team


class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'Test Team',
            'description': 'Test Description'
        }
    
    def test_create_team(self):
        response = self.client.post('/api/teams/', self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Test Team')
    
    def test_get_teams(self):
        Team.objects.create(**self.team_data)
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
