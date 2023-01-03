from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        exclude = ('id',)
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения модели Title."""
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        """возвращает в ответе вычисляемое поле - рейтинг произведения."""
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')

        if rating:
            return int(rating)

        return None


class TitleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания модели Title."""
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            GenreTitle.objects.create(genre=genre, title=title)
        return title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализер отзывов."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        exclude = ('title',)

    def get_title(self):
        request = self.context.get('request')
        return get_object_or_404(
            Title,
            pk=request.parser_context.get('kwargs').get('title_id')
        )

    def validate(self, attrs):
        if self.context.get('request').method == 'POST':
            user = self.context.get('request').user
            if Review.objects.filter(author=user, title=self.get_title()):
                raise serializers.ValidationError(
                    'Вы не можете создать два отзыва на одно произведение.'
                )

        return super().validate(attrs)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев к отзывам."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        exclude = ('review',)


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class GenerateCodeSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=queryset)]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=queryset)]
    )

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Служебное имя. Выберите другое')
        return data

    class Meta:
        fields = ("username", "email")
        model = User
