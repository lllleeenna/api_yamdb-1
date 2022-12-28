from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Titles(models.Model):
    pass


class Reviews(models.Model):
    """Модель отзывы на произведение."""
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва'
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date =models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации отзыва'
    )


class Comments(models.Model):
    """Модель комментарии к отзывам."""
    review = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    pub_date =models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации комментария'
    )


