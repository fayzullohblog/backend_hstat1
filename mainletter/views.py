from django.shortcuts import render
from rest_framework import generics

from django.shortcuts import get_object_or_404

from .serializer import TypeLetterSerializer,TemplateSerializer,FullTemplateSerializer,TemplateCreateSerializer
from .models import TypeLetter,Template
from accountapp.models import MyUser

from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny
#  Create your views here.





# class ReportRetrieveView(generics.RetrieveAPIView):
#     serializer_class = ReportSerailizer
#     queryset = Report.objects.all()

#     def get(self, request, *args, **kwargs):
#         pk = self.kwargs.get('pk')  # Obyekt ID sini olish
#         instance=self.get_object_by_typeletter(pk)
#         if instance is not None:
#             serializer = self.get_serializer(instance,many=True)
#             return Response(serializer.data)
#         serializer=self.get_serializer(instance)
#         return Response(serializer.data)
    

#     def get_object_by_typeletter(self,pk):
#         try:
#             return self.queryset.filter(typeletter__id=pk)
        
#         except Report.DoesNotExist:
#             return None

# class TypleLetterListApiView(generics.ListAPIView):
#     serializer_class=TypeLetterSerializer
#     queryset=TypeLetter.objects.all()



# class TemplateUpdateView(generics.RetrieveUpdateAPIView):
#     serializer_class = TemplateSerializer
#     queryset = Template.objects.all()

#     def get(self, request, *args, **kwargs):
#         pk1 = self.kwargs.get('pk1')
#         template_instance = self.queryset.get(name__id=pk1)
#         print('-------->',template_instance)
#         serializer = self.serializer_class(template_instance)
#         return Response(serializer.data)

#     def update(self, request, *args, **kwargs):
#         pk1 = self.kwargs.get('pk1')

#         if pk1 is None:
#             return Response({'status':'don\'t gave name id'})
#         template_instance = self.queryset.get(name__id=pk1)

#         #Assuming the 'body' is a JSON field, use request.data to access it
#         body_data = request.data.get('body', None)
    
#         if body_data is not None:
#             template_instance.body = body_data
#             template_instance.save()

#         serializer = self.serializer_class(template_instance)
#         return Response(serializer.data)
    

class TypleLetterListApiView(generics.ListAPIView):
    serializer_class=TypeLetterSerializer
    queryset=TypeLetter.objects.all()
    permission_classes=[AllowAny]



class TemplateRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    permission_classes=[AllowAny]

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        template_instance = self.queryset.filter(typeletter__id=pk).all()
        
        serializer = self.serializer_class(template_instance,many=True)

        return Response(serializer.data)
    


class TemplateRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = FullTemplateSerializer
    queryset = Template.objects.all()
    permission_classes=[AllowAny]


    def get(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')
        

        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)

        typeletter = get_object_or_404(TypeLetter, id=typeletter_pk)
        template_instance = get_object_or_404(self.queryset, typeletter__name=typeletter, id=template_pk1)



        serializer = self.serializer_class(template_instance)
        return Response(serializer.data)
    

    def put(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')

        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)

        typeletter = get_object_or_404(TypeLetter, id=typeletter_pk)
        template_instance = get_object_or_404(self.queryset, typeletter__name=typeletter, id=template_pk1)

        request.session['template_pk1']=template_instance.id
        request.session['typeletter_pk']=typeletter.id


        body_data = request.data.get('body', None)

        if body_data is not None:
            template_instance.body = body_data
            template_instance.save()

        serializer = self.serializer_class(template_instance, partial=True)
        return Response(serializer.data)



class TemplateCreateView(generics.CreateAPIView):
    queryset=Template.objects.all()
    serializer_class=TemplateCreateSerializer
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):

        user=self.request.user
        typeletter_id=self.request.data.get('typeletter')
        title=self.request.data.get('title')
        body=self.request.data.get('body')

        try:
            typeletter_instance=TypeLetter.objects.get(id=typeletter_id)
        except TypeLetter.DoesNotExist:
            return Response({'error':'Invalid typeletter ID '}, status=400)

        query=Template.objects.create(
            typeletter=typeletter_instance,
            user=user,
            title=title,
            body=body,
        )
        serializer=self.serializer_class(query)
     

        return Response(serializer.data)








    

    

    


    
    





    



    




    
    











    
