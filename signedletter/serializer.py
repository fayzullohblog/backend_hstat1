from rest_framework import serializers
from .models import  SignedPdf
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
from letterapp.models import PdfFileTemplate


class PartyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['party_name']


class TypeLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeLetter
        fields=['name','id']


class TemplateSerializer(serializers.ModelSerializer): 
    typeletter=TypeLetterSerializer(read_only=True)
    class Meta:
        model=Template
        fields=['typeletter','id','title']


class PdfFileTemplateUnSignedSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    template=TemplateSerializer()
    class Meta:
        model=PdfFileTemplate
        fields=[
            'id',
            'username',
            'pdf_file',
            'template',
            'signed_state',
        ]



class PdfFileTemplateSignedSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    template=TemplateSerializer()
    class Meta:
        model=PdfFileTemplate
        fields=[
            'pdf_file',
            'user',
      
        ]

    
    

    