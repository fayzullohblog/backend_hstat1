from rest_framework import serializers
from .models import TypeLetter,Template

class TypleLetterAllFieldSerializer(serializers.ModelSerializer):
    pass


# class TypeLetterSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=TypeLetter
#         fields=['id','name']



# class ReportSerailizer(serializers.ModelSerializer):
#     typeletter=TypeLetterSerializer()
#     class Meta:
#         model=Report
#         fields=['typeletter','id','name']
#         depth=3


# class TemplateSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Template
#         fields=['id','name','body']










# 2



class TypeLetterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TypeLetter
        fields=['id','name']



# class ReportSerailizer(serializers.ModelSerializer):
#     typeletter=TypeLetterSerializer()
#     class Meta:
#         model=Report
#         fields=['typeletter','id','name']
#         depth=3


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



    