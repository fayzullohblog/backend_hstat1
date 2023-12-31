from .models import LetterInstruction
# from mainletter.models import Report
from mainletter.models import Zarik
from rest_framework import serializers

class LetterInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterInstruction
        fields = [
            'template',

            'company_name',
            'adress',
            'street',

            'inn_number',
            'litter_number',
            'phone_number',
            'soato',

            'email',
            'report_date',
            'created_date_add',
            'state',
            ]

class ExcelInnSerializer(serializers.Serializer):
    excel_file = serializers.FileField()






class ZarikUploadSerializer(serializers.Serializer):
    zarik_file = serializers.FileField()

class ZarikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zarik
        fields='__all__'


# -----------------------------------------------------
