from django.shortcuts import render
from rest_framework import  generics
from rest_framework.response import Response

from .models import SignedPdf
from .serializer import PartyUserSerializer,TemplateSerializer,TypeLetterSerializer
from letterapp.models import PdfFileTemplate
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
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
    

class SignedPdfListApiView(generics.ListAPIView):
    pass