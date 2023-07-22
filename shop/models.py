from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Product(models.Model):


    choise=[
    ('Laptop','Laptop'),
    ('Computer','Computer'),
    ('Phone','Phone'),
    ('Screen','Screen'),
    ]


    Name = models.CharField(max_length=60)
    Price = models.FloatField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='images/')
    Availability = models.BooleanField(default=True)
    Color=ColorField(default='#000000')
    Categore = models.CharField(max_length=50, choices=choise, blank=True, null=True)




    def __str__(self):
        return self.Name
