from django.db import models

# Create your models here.
class Wiki ( models.Model):
    body = models.CharField(max_length=500)
    
    