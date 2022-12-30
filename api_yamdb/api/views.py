from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from users.models import User, ConfirmationCode
from .serializers import UserSerializer, AdminSerializer
from rest_framework import viewsets
from django.contrib import action


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = 

    @action(url_path='me', methods=['get','patch'], detail=False, permission_classes = ())
    def perform_create(self, request): 
        pass

class TokenViewSet(viewsets.ModelViewSet):

    @action(url_path='signup', methods=['post'], detail=False, permission_classes = ())
    def generator_code(self, request):
        pass

    @action(url_path='signup', methods=['post'], detail=False, permission_classes = ())
    def generator_token(self, request):
        pass

def send_ConfirmationCode(user):
    confirmation_code = get_random_string(length=16)
   # ConfirmationCode.objects.create(user=user, code=confirmation_code)
    return send_mail(
            'Ваш код подтверждения',
            f'Код подтверждения: {confirmation_code}.',
            'from@yambd.com',
            ['{user.email}'],
            fail_silently=False,
        )
