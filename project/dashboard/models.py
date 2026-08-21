# dashboard/models.py

from django.db import models
from classes.models import Class  # Import Class from the classes app
from django.contrib.auth.models import User
from datetime import date

class Assignment(models.Model):
    """
    Assignment model for tracking homework and tasks
    """
    
    # Choices for priority
    PRIORITY_CHOICES = [
        ('high', 'High Priority'),
        ('medium', 'Medium Priority'),
        ('low', 'Low Priority'),
    ]
    
    # Choices for status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    
    # === Fields ===
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    # Foreign key to Class model from classes app
    class_assigned = models.ForeignKey(
        Class, 
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium'
    )
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    
    points = models.IntegerField(default=100)
    
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )
    
    # === Properties ===
    @property
    def days_left(self):
        """Days until due date"""
        delta = self.due_date - date.today()
        return delta.days
    
    @property
    def is_overdue(self):
        """Check if overdue"""
        return self.due_date < date.today() and self.status != 'completed'
    
    @property
    def is_due_today(self):
        """Check if due today"""
        return self.due_date == date.today()
    
    # === String representation ===
    def __str__(self):
        return f"{self.title} ({self.class_assigned.name})"
    
    # === Meta ===
    class Meta:
        ordering = ['due_date']