from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import LetterInstruction,Zarik,ReportCategory
from .serializer import LetterInstructionSerializer,ExcelUploadSerializer,ZarikSerializer,ZarikUploadSerializer
from rest_framework import generics, status
from reportlab.pdfgen import canvas
import os
from django.template.loader import render_to_string
from weasyprint import HTML
from datetime import datetime
# from config.settings import settings
# print(settings.MEDIA_URL)
                                             
# print('------->',settings.MEDIA_ROOT)



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

# class ExcelUploadAPIView(generics.CreateAPIView):
#     serializer_class = ExcelUploadSerializer
#     queryset = LetterInstruction.objects.all()
#     permission_classes = [IsAdminUser]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'error': 'Is valid xato'}, status=status.HTTP_400_BAD_REQUEST)

#         name = serializer.validated_data['name']
#         excel_file = serializer.validated_data['excel_file']
#         template = serializer.validated_data['template']

#         if not excel_file:
#             return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)
        
#         if not template:
#             return Response({"error": "Xat shabloni notug'ri."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Excel faylni o'qish
#             df = pd.read_excel(excel_file)
#             inn_numbers = df['inn_number'].tolist()

#             # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
#             report_category = ReportCategory.objects.get(name=name)
#             filtered_zarik = Zarik.objects.filter(inn_number__in=inn_numbers).all()

#             # filtered_zarik dan olingan ma'lumotlarni LetterInstruction ga o'tkazish
#             objects = [
#                 LetterInstruction(
#                     report_category=report_category,
#                     company_name=record.company_name,
#                     inn_number=record.inn_number,
#                     address=record.adress,  # O'zgartirilgan maydon nomi
#                     street=record.street,
#                     phone_number=record.phone_number,
#                     soato=record.soato,
#                 )
#                 for record in filtered_zarik
#             ]

#             # LetterInstruction obyektlarini bazaga yozish
#             LetterInstruction.objects.bulk_create(objects)

#             # filtered_letter olish
#             filtered_letter = LetterInstruction.objects.filter(inn_number__in=inn_numbers).all()

#             # PDF faylini yaratish va u yerga saqlash funksiyasini chaqirish
#             pdf_file_path = self.create_pdf(template, filtered_letter)

#             # Agar pdf yaratish muvaffaqiyatli bo'lsa
#             if pdf_file_path:
#                 # PDF manzilini olish
#                 pdf_url = request.build_absolute_uri(pdf_file_path)

#                 # PDF manzilini javob qilish
#                 return Response({'pdf_url': pdf_url}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'PDF fayl yaratishda xato'}, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

#     def create_pdf(self, template, filtered_letter):
#         try:
#             # HTML-ga o'tkazish
#             html_content = render_to_string(template, {'filtered_letter': filtered_letter})

#             # PDF faylini yaratish
#             pdf_content = HTML(string=html_content).write_pdf()

#             # PDF faylini bazaga saqlash
#             pdf_file_name = f'output_{datetime.now().strftime("%Y%m%d%H%M%S")}.pdf'
#             pdf_file_path = os.path.join(settings.MEDIA_ROOT, pdf_file_name)

#             with open(pdf_file_path, 'wb') as pdf_file:
#                 pdf_file.write(pdf_content)

#             return pdf_file_path

#         except Exception as e:
#             return None


class ExcelUploadAPIView(generics.CreateAPIView):
    serializer_class = ExcelUploadSerializer
    queryset=LetterInstruction.objects.all()
    permission_classes=[IsAdminUser]
     
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():   
            name=serializer.validated_data['name']
            excel_file=serializer.validated_data['excel_file']
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
                report_category=ReportCategory.objects.get(name=name)
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