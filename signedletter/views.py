from django.shortcuts import render
from rest_framework.generics import  CreateAPIView
from .models import SignedPdf
from .serializer import SignedPdfSerializer

# Create your views here.


class SignedCreateApiView(CreateAPIView):
    serializer_class=SignedPdfSerializer
    queryset=SignedPdf.objects.all()


