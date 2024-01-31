from django.shortcuts import render
from rest_framework import  generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import SignedPdf
from letterapp.models import PdfFileTemplate
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
from rest_framework import status
from .serializer import (
                PartyUserSerializer,
                TemplateSerializer,
                TypeLetterSerializer,
                PdfFileTemplateUnSignedSerializer,
                # PdfFileTemplateUnsignedSerializer,
                PdfFileTemplateSignedSerializer,
                 )     
# Create your views here.



class PartyUserListApiView(generics.ListAPIView):
    serializer_class=PartyUserSerializer
    queryset=MyUser.objects.all()


    def get(self, request, *args, **kwargs):
        queryset=self.queryset.filter(is_admin=True,is_superuser=False,is_active=True)
        serializer=self.serializer_class(queryset,many=True).data
        return Response({'result':serializer})


class TypeLetterListApiView(generics.ListAPIView):
    serializer_class=TypeLetterSerializer
    queryset=TypeLetter.objects.all()


class TemplateListApiView(generics.ListAPIView):
    serializer_class=TemplateSerializer
    queryset=Template.objects.all()

    def get_queryset(self):
        typeletter_id=self.kwargs['pk']
        queryset=self.queryset.filter(typeletter_id=typeletter_id).all()

        return queryset


class PdfFileTemplateUnsignedListApiView(generics.ListAPIView):
    serializer_class=PdfFileTemplateUnSignedSerializer
    queryset = PdfFileTemplate.objects.all()

    def get(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')

        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)

        
        pdffiletemplate=self.queryset.filter(
            template_id=template_pk1,
            user=self.request.user,
            signed_state=False,
            template__typeletter_id=typeletter_pk)
       



        serializer = self.serializer_class(pdffiletemplate,many=True)
        return Response(serializer.data)

class PdfFileTemplateUnsignedDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class=PdfFileTemplateUnSignedSerializer
    queryset = PdfFileTemplate.objects.all()



class PdfFileTemplateSignedUpdateApiView(generics.UpdateAPIView):
    serializer_class=PdfFileTemplateSignedSerializer
    queryset=PdfFileTemplate.objects.all()


    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)



