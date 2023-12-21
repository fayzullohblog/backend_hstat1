from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from mainletter.models import Report
from .models import LetterInstruction
from mainletter.models import Zarik
from .serializer import LetterInstructionSerializer,ExcelUploadSerializer,ZarikSerializer,ZarikUploadSerializer
from rest_framework import generics, status
from reportlab.pdfgen import canvas
import os
from django.template.loader import render_to_string
from weasyprint import HTML
from datetime import datetime



class ZarikCreateApiView(generics.CreateAPIView):
    serializer_class=ZarikUploadSerializer
    queryset=Zarik.objects.all()
    permission_classes=[IsAdminUser]

    def post(self, request, *args, **kwargs):
        excel_file = request.data.get('zarik_file')
        try:
            df = pd.read_excel(excel_file)

            row,_=df.shape
            
            records = df.to_dict(orient='records')
            objetcs=[Zarik(**record) for record in records]
            
            Zarik.objects.bulk_create(objetcs)
            queryset=self.get_queryset()[:row]
            
            serializer=ZarikSerializer(queryset,many=True)  
            return Response({"Successful": f"{row} ta companya bazaga saqlandi"}, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({'error':f'Zarik bazani  saqlashda xatolik {e}'},status=status.HTTP_404_NOT_FOUND)


class LetterInstructionView(generics.CreateAPIView):
    serializer_class = ExcelUploadSerializer
    queryset=LetterInstruction.objects.all()
    permission_classes=[IsAdminUser]
     
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():   
            name=serializer.validated_data['name']
            excel_file=serializer.validated_data['excel_inn']
            template=serializer.validated_data['template']
       
            # PDF fayllaga saqlash


            if not excel_file:
                return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)
            
            if not template:
                return Response({"error": "Xat shabloni notug'ri."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Excel faylni o'qish
                df = pd.read_excel(excel_file)
                inn_number = df['inn_number'].tolist()
                # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
                report_category=Report.objects.get(name=name)
                filtered_zarik = Zarik.objects.filter(inn_number__in=inn_number).all()
                
                objects=[LetterInstruction(
                                        report_category=report_category,
                                        company_name=record.company_name,
                                        inn_number=record.inn_number,
                                        adress=record.adress,
                                        street=record.street,
                                        phone_number=record.phone_number,
                                        soato=record.soato,
                                        )
                            for record in filtered_zarik 
                        ]
                
                
                LetterInstruction.objects.bulk_create(objects)
           

                filtered_letter=LetterInstruction.objects.filter(inn_number__in=inn_number).all()
                serializer = LetterInstructionSerializer(filtered_letter, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Is validda xato'})


def tiny(request):
    return render(request=request,template_name='tiny.html')