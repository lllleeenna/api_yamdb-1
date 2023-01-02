from users.models import User, CHOICES_ROLE
from rest_framework import serializers


class AdminSerializer(serializers.ModelSerializer):
    role = serializers.CharField(choices=CHOICES_ROLE, default='user')
    
    class Meta:
        fields = ('__all__')
        model = User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(choices=CHOICES_ROLE, default='user')
    
    class Meta:
        fields = ('__all__')
        model = User

    def validate(self, data):
        if data.username=='me':
            raise serializers.ValidationError('Служебное имя. Выберите другое')
        return data
        