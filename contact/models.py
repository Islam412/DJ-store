from django.db import models

# Create your models here.

class Info(models.Model):
    Adrees = models.TextField(max_length=1000)
    Email = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    def __str__(self):
        return self.Adrees