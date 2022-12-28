from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = 

    def GenerateCode(self, request):

    


def send_ConfirmationCode(user):
    confirmation_code = get_random_string(length=16)
    ConfirmationCode.objects.create(user=user, code=confirmation_code)
    return send_mail(
            'Ваш код подтверждения',
            f'Код подтверждения: {confirmation_code}.',
            'from@yambd.com',
            ['{user.email}'],
            fail_silently=False,
        )
