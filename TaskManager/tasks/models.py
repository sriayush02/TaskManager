from django.db import models
from django.contrib.auth.models import User

# Task Model
class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    
    TASK_TYPE_CHOICES = [
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('OPTIONAL', 'Optional'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default='NORMAL')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='PENDING')
    
    # ManyToManyField to relate Task with Users
    assigned_users = models.ManyToManyField(User, related_name='tasks')  # Correct configuration

    def __str__(self):
        return self.name



# Create your models here.
