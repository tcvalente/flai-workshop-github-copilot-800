from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, default='')
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=150, blank=True, default='')
    last_name = models.CharField(max_length=150, blank=True, default='')
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        ordering = ['created_at']

    def __str__(self):
        return self.email
