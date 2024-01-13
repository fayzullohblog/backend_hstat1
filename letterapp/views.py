from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from rest_framework.permissions import AllowAny

# from mainletter.models import Report
from .models import (
                        LetterInstruction,
                        PdfFileTemplate,
                    )
from mainletter.models import Zarik,Template
from .serializer import (
                        LetterInstructionSerializer,
                        ExcelInnSerializer,
                        ZarikSerializer,
                        ZarikUploadSerializer,
                        PdfFileTemplateSerializer,
                        )
from rest_framework import generics, status
from django.template.loader import render_to_string

import pdfkit
from django.template.loader import get_template
from .generate_pdf import generate_pdf

class ZarikCreateApiView(generics.CreateAPIView):
    serializer_class=ZarikUploadSerializer
    queryset=Zarik.objects.all()
    permission_classes=[AllowAny]

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

# bedkor ilinadi, O'rniga PdffileTemplateView qilindi
class LetterInstructionView(generics.CreateAPIView):
    serializer_class = ExcelInnSerializer
    queryset=LetterInstruction.objects.all()
    permission_classes=[AllowAny]
    
    def post(self, request, *args, **kwargs):
       

        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():   

            excel_file=serializer.validated_data['excel_file']
          
            #PDF fayllaga saqlash

            if not excel_file:
                return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Excel faylni o'qish
                df = pd.read_excel(excel_file)
                inn_number = df['inn_number'].tolist()
                # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
              
                filtered_zarik = Zarik.objects.filter(inn_number__in=inn_number).all()
              
                template_pk1=request.session.get('template_pk1')
                typeletter_pk=request.session.get('typeletter_pk')
               
                domain_name=request.META['HTTP_HOST']
                
           
                                
                objects = []
                file_name=LetterInstruction.objects.pdf_file_count()
                
    
                for record in filtered_zarik:
                    file_name+=1
                    obj = LetterInstruction(
                        template_id=template_pk1,
                        company_name=record.company_name,
                        adress=record.adress,
                        street=record.street,
                        inn_number=record.inn_number,
                        phone_number=record.phone_number,
                        soato=record.soato,
                        email=record.email,
                        # pdf_file=generate_pdf(
                        #     template_pk1=template_pk1,
                        #     typeletter_pk=typeletter_pk,
                        #     user=request.user,
                        #     file_name=file_name,
                        #     adress=record.adress,
                        #     street=record.street,
                        #     company_name=record.company_name,
                        #     inn_number=record.inn_number,
                        #     phone_number=record.phone_number,                          
                        #     update_date=record.update_date,
    
                            
                        #     )
                    )
                    objects.append(obj)
                
                LetterInstruction.objects.bulk_create(objects)


                inn_count=filtered_zarik.count()
            
                filtered_letter=LetterInstruction.objects.filter(inn_number__in=inn_number).all().order_by('-create_date')[:inn_count]
                serializer = LetterInstructionSerializer(filtered_letter, many=True)
         

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Is validda xato'})



def tiny(request):
    return render(request=request,template_name='tiny.html')


class PdfFileTemplateView(generics.CreateAPIView):
    serializer_class = ExcelInnSerializer
    queryset=PdfFileTemplate.objects.all()
    permission_classes=[AllowAny]
    
    def post(self, request, *args, **kwargs):
       

        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():  

            excel_file=serializer.validated_data['excel_file']
            print('---------2',excel_file)
          
            #PDF fayllaga saqlash

            if not excel_file:
                return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Excel faylni o'qish
                df = pd.read_excel(excel_file)
                inn_number = df['inn_number'].tolist()
                # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
              
                filtered_zarik = Zarik.objects.filter(inn_number__in=inn_number).all()
                if not filtered_zarik.exists():
                    return Response(data={'message':'Zarik baza yaratilmagan'})
              
                template_pk1=request.session.get('template_pk1')
                typeletter_pk=request.session.get('typeletter_pk')
               
                domain_name=request.META['HTTP_HOST']
                
           
                                
                objects = []
                file_name=PdfFileTemplate.objects.pdf_file_count()
                
    
                for record in filtered_zarik:
                    file_name+=1
                    obj = PdfFileTemplate(
                        template_id=template_pk1,
                        # company_name=record.company_name,
                        # adress=record.adress,
                        # street=record.street,
                        inn_number=record.inn_number,
                        soato=record.soato,
                        # email=record.email,
                        pdf_file=generate_pdf(
                            template_pk1=template_pk1,
                            typeletter_pk=typeletter_pk,
                            request=request,
                            file_name=file_name,

                            adress=record.adress,
                            street=record.street,
                            company_name=record.company_name,
                            inn_number=record.inn_number,
                            phone_number=record.phone_number, 
                                                     
                          
    
                            
                            )
                    )
                    objects.append(obj)
                
                PdfFileTemplate.objects.bulk_create(objects)


                inn_count=filtered_zarik.count()
            
                filtered_letter=PdfFileTemplate.objects.filter(inn_number__in=inn_number).all().order_by('-create_date')[:inn_count]
                serializer = PdfFileTemplateSerializer(filtered_letter, many=True)
         

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Is validda xato'})

