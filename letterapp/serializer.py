from .models import LetterInstruction
# from mainletter.models import Report
from mainletter.models import Zarik
from rest_framework import serializers

class LetterInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterInstruction
        fields = ['user','inn_number','litter_number','stir_number','phone_number','report_category','letter_name','company_name','adress','street','report_date','created_date_add']

class ExcelUploadSerializer(serializers.Serializer):
    excel_file = serializers.FileField()
    template=serializers.CharField()
    name=serializers.CharField()


# class CreateTemplateModelSerializer(serializers.ModelSerializer):
#     excel_file = serializers.FileField()
#     class Meta:
#         models=Report
#         fields=['name','typeletter']




class ZarikUploadSerializer(serializers.Serializer):
    zarik_file = serializers.FileField()

class ZarikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zarik
        fields='__all__'


# -----------------------------------------------------
