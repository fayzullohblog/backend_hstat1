from django.shortcuts import render
from rest_framework import  generics
from rest_framework.views import APIView
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
from .persmissions import OnlySuperUserOrStaff
from rest_framework.permissions import IsAuthenticated
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
    serializer_class=TypeLetterSerializer
    queryset=TypeLetter.objects.all()
    permission_classes=[IsAuthenticated,OnlySuperUserOrStaff]

    def get(self, request, *args, **kwargs):    
        request.session['staff_username']=self.kwargs['staff_username']
        return super().get(request, *args, **kwargs)


    
    


class TemplateListApiView(generics.ListAPIView):
    serializer_class=TemplateSerializer
    queryset=Template.objects.all()



    def get(self, request, *args, **kwargs):
        typeletter_id=self.kwargs['pk']
        staff_username=request.session['staff_username']


        queryset=self.queryset.filter(typeletter_id=typeletter_id,user__username=staff_username).all()
        serializer=self.serializer_class(instance=queryset,many=True)
        
        return Response(serializer.data)


# class PdfFileTemplateUnsignedListApiView(generics.ListAPIView):
#     serializer_class=PdfFileTemplateUnSignedSerializer
#     queryset = PdfFileTemplate.objects.all()

#     def get(self, request, *args, **kwargs):
#         template_pk1 = self.kwargs.get('pk1')
#         typeletter_pk = self.kwargs.get('pk')

#         if template_pk1 is None or typeletter_pk is None:
#             return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)

        
#         pdffiletemplate=self.queryset.filter(
#             template_id=template_pk1,
#             user=self.request.user,
#             signed_state=False,
#             template__typeletter_id=typeletter_pk)
       



#         serializer = self.serializer_class(pdffiletemplate,many=True)
#         return Response(serializer.data)


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

        
        pdffiletemplate=self.get_queryset().filter(
            template_id=template_pk1,
            user__username=self.request.session['staff_username'],
            signed_state=False,
            template__typeletter_id=typeletter_pk)

        serializer = self.serializer_class(pdffiletemplate,many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')

        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)

        typeletter_pk = get_object_or_404(TypeLetter, id=typeletter_pk)
        template_instance = self.get_queryset().filter(
            template_id=template_pk1,
            user=self.request.user,
            signed_state=False,
            template__typeletter_id=typeletter_pk    

        )



        serializer = self.serializer_class(template_instance, partial=True)
        return Response(serializer.data)









class PdfFileTemplateUnsignedDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class=PdfFileTemplateUnSignedSerializer
    queryset = PdfFileTemplate.objects.all()



class PdfFileTemplateSignedUpdateApiView(generics.UpdateAPIView):
    serializer_class=PdfFileTemplateSignedSerializer
    queryset=PdfFileTemplate.objects.all()



