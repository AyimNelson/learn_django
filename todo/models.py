from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"
    