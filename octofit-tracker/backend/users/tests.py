from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from teams.models import Team


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team', description='Test Description')
        self.user_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'testpass123',
            'team': self.team.id
        }
    
    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')
    
    def test_get_users(self):
        User.objects.create(**self.user_data)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
