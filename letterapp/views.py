from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from rest_framework.permissions import IsAdminUser

from .models import LetterInstruction
from .serializer import LetterInstructionSerializer,ExcelUploadSerializer
from rest_framework import generics, status

class ExcelUploadAPIView(generics.CreateAPIView):
    serializer_class = ExcelUploadSerializer
    queryset=LetterInstruction.objects.all()
    permission_classes=[IsAdminUser]
     
    def create(self, request, *args, **kwargs):    

        excel_file = request.data.get('excel_file')

        if not excel_file:
            return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Excel faylni o'qish
            df = pd.read_excel(excel_file)
            inn_numbers = df['inn_number'].tolist()

            # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
            filtered_letters = LetterInstruction.objects.filter(inn_number__in=inn_numbers)

            # Filtrlangan ma'lumotlarni serializatsiya qilish
            serializer = LetterInstructionSerializer(filtered_letters, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


 