from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Comment, Review, Title


class TitleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        """возвращает в ответе вычисляемое поле - рейтинг произведения."""
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')

        if rating:
            return int(rating)

        return None


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
