from rest_framework import serializers
from .models import TypeLetter,Template


class TypeLetterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TypeLetter
        fields=['id','name']


class TemplateSerializer(serializers.ModelSerializer):
    typeletter=TypeLetterSerializer()
    class Meta:
        model=Template
        fields=['typeletter','id','title']


class FullTemplateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Template
        fields=['id','title','body']
        read_only_fields=('title',)


class TemplateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Template
        fields=['typeletter','title','body']

    