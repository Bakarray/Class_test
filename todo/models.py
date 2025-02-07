from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=priority_choices, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title