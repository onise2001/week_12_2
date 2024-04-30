from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    date = models.CharField(max_length=50)
