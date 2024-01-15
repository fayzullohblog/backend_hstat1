from rest_framework import serializers
from .models import  SignedPdf


class SignedPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignedPdf
        fields=[
            'pdf',
        ]