from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user) -> Token:
        token=super().get_token(user)
        token['username']=user.username
        # token['is_admin']=user.is_admin
        token['is_staff']=user.is_staff
        token['is_superuser']=user.is_superuser
        token['is_active']=user.is_active
        token['is_boss']=user.is_active

        return token
        
        

class MyUserSerializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'

    def create(self, validated_data):

        user = MyUser.objects.create_user(
            validated_data['username'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            )
        return user
