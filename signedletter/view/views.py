from django.shortcuts import render
from rest_framework import  generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ..models import SignedPdf
from letterapp.models import PdfFileTemplate
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
from rest_framework import status
from ..serializer import (
                PartyUserSerializer,
                SignedTemplateSerializer,
                SignedTypeLetterSerializer,
                PdfFileTemplateUnSignedSerializer,
                # PdfFileTemplateUnsignedSerializer,
                PdfFileTemplateSignedSerializer,
                 )     
from ..persmissions import OnlySuperUserOrStaff
from rest_framework.permissions import IsAuthenticated

from ..pdf_parser import PdfParser
# Create your views here.



class PartyUserListApiView(generics.ListAPIView):
    serializer_class=PartyUserSerializer
    queryset=MyUser.objects.all()
    permission_classes=[IsAuthenticated,OnlySuperUserOrStaff]
    

    def get(self, request, *args, **kwargs):
        queryset=self.queryset.filter(is_admin=True,is_superuser=False,is_active=True)
        serializer=self.serializer_class(queryset,many=True).data
        return Response({'result':serializer})


class TypeLetterListApiView(generics.ListAPIView):
    serializer_class=SignedTypeLetterSerializer
    queryset=TypeLetter.objects.all()
    permission_classes=[IsAuthenticated,OnlySuperUserOrStaff]

    def get(self, request, *args, **kwargs):    
        request.session['staff_username']=self.kwargs['staff_username']
        return super().get(request, *args, **kwargs)


    
    


class TemplateListApiView(generics.ListAPIView):
    serializer_class=SignedTemplateSerializer
    queryset=Template.objects.all()



    def get(self, request, *args, **kwargs):
        typeletter_id=self.kwargs['pk']
        try:
            staff_username=request.session['staff_username']
        except:
            return Response("Siz bo'limdi tanlamasdan, xatlar turini ko'ra olmaysiz, birinchi  bo'limni tanlang keyin xatlarni ko'ra olasiz")
        

        queryset=self.queryset.filter(typeletter_id=typeletter_id,user__username=staff_username).all()
        serializer=self.serializer_class(instance=queryset,many=True)
        
        return Response(serializer.data)


class PdfFileTemplateUnsignedListApiView(APIView):
    serializer_class=PdfFileTemplateUnSignedSerializer


    def get_queryset(self):
        # queryset = PdfFileTemplate.objects.all()
        return PdfFileTemplate.objects.all()
    
    def get(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')
        
        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            staff_username=request.session['staff_username']
        except:
            return Response("Siz bo'limdi tanlamasdan, bo'limga tegishli xisobatlarni ko'ra olmaysiz, birinchi  bo'limni tanlang keyin xatlarni ko'ra olasiz")
        
        
        pdffiletemplate=self.get_queryset().filter(
            template_id=template_pk1,
            user__username=staff_username,
            signed_state=False,
            template__typeletter_id=typeletter_pk)

        serializer = self.serializer_class(pdffiletemplate,many=True)
        return Response(serializer.data)


class PdfFileTemplateUnsignedDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class=PdfFileTemplateUnSignedSerializer
    queryset = PdfFileTemplate.objects.all()





class PdfFileTemplateSignedUpdateApiView(APIView):
    
    def put(self, request, *args, **kwargs):
        data = request.data
        pdf_file_updates = data.get('pdf_file_updates', [])  # List of dictionaries with 'id', 'pdf_file', and 'signed_state'
        for update_data in pdf_file_updates:
            pdf_file_id = update_data.get('id')
            # pdf_file_path = update_data.get('pdf_file')
            signed_state = update_data.get('signed_state')

            try:
                pdf_file_template = PdfFileTemplate.objects.get(id=pdf_file_id,signed_state=signed_state)
                
            except PdfFileTemplate.DoesNotExist:
                return Response({'status': f'PdfFileTemplate with id {pdf_file_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)


            pdf_file_path=pdf_file_template.pdf_file
            
            new_folder_name=str(pdf_file_path).split('/')
            print('--------',new_folder_name)

            #  shu yerga kelib qolgan edik



        return Response({'status': 'Successfully updated'}, status=status.HTTP_200_OK)
    

