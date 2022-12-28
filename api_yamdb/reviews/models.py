from django.db import models
from .validators import validate_year


class Category(models.Model):
    """Модель Категории."""
    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
        help_text='Укажите категорию',
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        help_text='Укажите адрес',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Genre(models.Model):
    """Модель Жанры."""
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
        help_text='Укажите жанр',
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        help_text='Укажите адрес',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Title(models.Model):
    """Модель Произведения."""
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведение',
        help_text='Введите название произведения',
        unique=True
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска произведения',
        help_text='Введите год выпуска',
        db_index=True,
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Введите текст описания',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
        verbose_name='Жанры произведения',
        help_text='Укажите жaнры'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория произведения',
        help_text='Укажите категорию',
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class GenreTitle(models.Model):
    """Модель для связи id произведения и id его жанра."""
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'Жанр: {self.genre}, произведение: {self.title}'
