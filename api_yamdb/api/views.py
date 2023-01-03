from rest_framework import viewsets, status, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.core.mail import send_mail
from users.models import User

from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitleCreateSerializer,
    UserSerializer,
    AdminSerializer,
    TokenSerializer,
    GenerateCodeSerializer
)
from .filters import TitleFilter
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .permissions import (
    IsAdmin,
    IsAdminOrReadOnly,
    IsModeratorOrAdmin,
    IsAuthor,
    IsAdminOrSuperuserOrReadOnly
)
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrSuperuserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrSuperuserOrReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrSuperuserOrReadOnly]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'DELETE'):
            return TitleCreateSerializer
        return TitleSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'username'

    def perform_create(self, serializer):
        if not serializer.validated_data.get('role'):
            serializer.validated_data['role'] = 'user'
        User.objects.create_user(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        url_path='me',
        methods=['get', 'patch'],
        detail=False,
        permission_classes=(IsAuthor,)
    )
    def show_user_profile(self, request):
        if request.method == "GET":
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "PATCH":
            serializer = UserSerializer(
                request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def generator_code(request):
    serializer = GenerateCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    username = serializer.validated_data["username"]
    user = get_object_or_404(User, username=username)
    send_ConfirmationCode(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def generator_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data["username"]
    code = serializer.validated_data["confirmation_code"]
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, code):
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_ConfirmationCode(user):
    confirmation_code = default_token_generator.make_token(user)
    return send_mail(
            'Ваш код подтверждения',
            f'Код подтверждения для {user.username} : {confirmation_code}.',
            'from@yambd.com',
            ['{user.email}'],
            fail_silently=False,
    )
