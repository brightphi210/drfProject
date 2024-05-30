from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.title
    
    
    