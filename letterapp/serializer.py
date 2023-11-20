from .models import LetterInstruction
from rest_framework import serializers

class LetterInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterInstruction
        fields = ['user','inn_number','litter_number','stir_number','phone_number','report_name','letter_name','company_name','adress','street','report_date','created_date_add']

class ExcelUploadSerializer(serializers.Serializer):
    excel_file = serializers.FileField()
