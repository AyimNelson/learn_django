from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.title}"
    