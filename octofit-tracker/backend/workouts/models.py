from django.db import models

class Workout(models.Model):
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    activity_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    duration = models.IntegerField(help_text='Suggested duration in minutes')
    calories_estimate = models.IntegerField(help_text='Estimated calories burned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'
        ordering = ['difficulty', 'title']

    def __str__(self):
        return f"{self.title} ({self.difficulty})"
