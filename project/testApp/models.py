from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    class Meta:
        unique_together = ('name', 'code', 'section')
    
    def __str__(self):
        return f"{self.name} ({self.code}) - Section {self.section}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"