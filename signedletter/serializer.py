from rest_framework import serializers
from .models import  SignedPdf
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter



class PartyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['party_name']


class TypeLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeLetter
        fields=['name','id']


class TemplateSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Template
        fields=['title','typeletter','user']


