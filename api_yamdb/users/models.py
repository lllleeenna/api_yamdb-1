from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = ['user','admin','moderator']

class User(AbstractUser):
    username = models.CharField(max_length=150, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    bio = models.TextField(null=True)
    role = models.CharField(max_length=16, choices=CHOICES, default='user')

    def __str__(self):
        return (self.username, self.email)
