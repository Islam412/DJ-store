from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any custom fields here if needed
    username = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_image')
    PhoneNumber = models.CharField(max_length=50)
    age = models.CharField(max_length=10)

    # Add unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )

    def __str__(self):
        return self.username
