from users.models import User
from rest_framework import serializers

from rest_framework.validators import UniqueValidator


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
    queryset=User.objects.all()
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=queryset)]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=queryset)]
    )

    def validate(self, data):
        if data['username']=='me':
            raise serializers.ValidationError('Служебное имя. Выберите другое')
        return data
    
    class Meta:
        fields = ("username", "email")
        model = User