from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user) -> Token:
        token=super().get_token(user)
        token['username']=user.username
        token['state']=user.state
        token['level']=user.role_user

        return token
        
        

class MyUserSerializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'

    def create(self, validated_data):
        d=validated_data['password']
        user = MyUser.objects.create_user(
            validated_data['username'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            )
        return user
