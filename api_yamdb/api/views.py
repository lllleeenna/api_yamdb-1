from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review, Title
from .permissions import ReviewCommentPermission
from .serializers import CommentSerializer, ReviewSerializer, TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Title.objects.all()


class ReviewsViewSet(viewsets.ModelViewSet):
    """Получение списка отзывов, одного отзыва. Создание отзыва.
    Изменение и удаление отзыва.
    """

    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReviewCommentPermission,)

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=self.get_title()
        )

    def get_queryset(self):
        return self.get_title().reviews.all()


class CommentsViewSet(viewsets.ModelViewSet):
    """Получение списка комментариев к отзыву, одного комментария.
    Создание комментария. Изменение и удаление комментария.
    """

    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReviewCommentPermission,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        )

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=title
        )
        return review.comments.all()
