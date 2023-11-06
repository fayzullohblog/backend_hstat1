from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework.serializers import ModelSerializer
from .models import MyUser


class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user) -> Token:
        print('----',user.username)
        token=super().get_token(user)
        token['username']=user.username
        token['state']=user.state
        token['level']=user.role_user

        return token
        
        

class MyUserSerializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'