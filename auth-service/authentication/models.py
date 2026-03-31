from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model with role field"""
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('staff', 'Staff'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.username} ({self.role})"
