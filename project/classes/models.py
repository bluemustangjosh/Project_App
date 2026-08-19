from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code}) - Section {self.section}"
