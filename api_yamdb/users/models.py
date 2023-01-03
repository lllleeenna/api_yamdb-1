from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES_ROLE = (
    ('user', 'Пользователь'),
    ('admin', 'Администратор'),
    ('moderator', 'Модератор')
)


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(
        null=True,
        verbose_name="О себе:",
        help_text="Напишите несколько строк о себе"
    )
    role = models.CharField(
        max_length=16,
        choices=CHOICES_ROLE,
        default='user'
    )

    def __str__(self):
        return f'username: {self.username}, email: {self.email}'