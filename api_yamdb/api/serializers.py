from rest_framework import serializers

from reviews.models import Category, Genre, GenreTitle, Title
from users.models import User
from rest_framework.validators import UniqueValidator


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
    # rating

    class Meta:
        fields = '__all__'
        model = Title


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
