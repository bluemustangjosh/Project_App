from django.db import models
from classes.models import Class   # <-- IMPORTANT: use the Class model from the classes app

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)

    # Login fields
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    # Many-to-many relationship to the Class model in the classes app
    classes = models.ManyToManyField(Class, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

