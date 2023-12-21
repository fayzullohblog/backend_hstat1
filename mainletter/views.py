from django.shortcuts import render
from rest_framework import generics

from django.shortcuts import get_object_or_404
from .serializer import TypeLetterSerializer,TemplateSerializer,FullTemplateSerializer
from .models import TypeLetter,Template
from rest_framework.response import Response
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



class TemplateRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        template_instance = self.queryset.filter(typeletter__id=pk).all()
        serializer = self.serializer_class(template_instance,many=True)
        return Response(serializer.data)
    

    

class TemplateRetrieveUpdateAPIView(generics.GenericAPIView):
    serializer_class = FullTemplateSerializer
    queryset = Template.objects.all()

    def get(self, request, *args, **kwargs):
        pk1 = self.kwargs.get('pk1')
        template_instance = self.queryset.get(id=pk1)

        serializer = self.serializer_class(template_instance)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        pk1 = self.kwargs.get('pk1')

        if pk1 is None:
            return Response({'status':'don\'t gave name id'})
        template_instance = self.queryset.get(id=pk1)
        print('')
        body_data = request.data.get('body', None)
        
        if body_data is not None:
            template_instance.body = body_data
            template_instance.save()

        serializer = self.serializer_class(template_instance)
        return Response(serializer.data)
    





    

    

    


    
    





    



    




    
    











    
