from django.urls import path
from .views import TemplateRetrieveAPIView,TypleLetterListApiView,TemplateRetrieveUpdateAPIView

urlpatterns = [
    path('typeletter/',TypleLetterListApiView.as_view()),
    path('typeletter/<int:pk>/',TemplateRetrieveAPIView.as_view()),
    path('typeletter/<int:pk>/<int:pk1>/',TemplateRetrieveUpdateAPIView.as_view()),
    
]