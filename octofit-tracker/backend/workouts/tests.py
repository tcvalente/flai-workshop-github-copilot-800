from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Workout


class WorkoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'title': 'Morning Run',
            'description': 'A refreshing morning run',
            'activity_type': 'running',
            'difficulty': 'beginner',
            'duration': 30,
            'calories_estimate': 300
        }
    
    def test_create_workout(self):
        response = self.client.post('/api/workouts/', self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Workout.objects.get().title, 'Morning Run')
    
    def test_get_workouts(self):
        Workout.objects.create(**self.workout_data)
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
