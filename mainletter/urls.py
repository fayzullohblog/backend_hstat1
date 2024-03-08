from django.urls import path
from .views import(TemplateRetrieveAPIView,TypleLetterListApiView,
                   TemplateRetrieveUpdateAPIView,TemplateCreateView,
                   ZarikListApiView,ZarikUpdateApiView
                   )





urlpatterns = [
    path('typeletter/',TypleLetterListApiView.as_view()),
    path('template-create/',TemplateCreateView.as_view()),
    path('typeletter/zarik-get/',ZarikListApiView.as_view()),
     path('typeletter/zarik-update/<int:pk>/',ZarikUpdateApiView.as_view()),
    path('typeletter/<int:pk>/',TemplateRetrieveAPIView.as_view()),
    path('typeletter/<int:pk>/<int:pk1>/',TemplateRetrieveUpdateAPIView.as_view()),
    
    ]