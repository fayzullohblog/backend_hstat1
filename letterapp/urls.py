from django.urls import path
from .views import LetterInstructionView,ZarikCreateApiView,tiny,PdfFileTemplateView

urlpatterns =  [
    path('get_inn/',PdfFileTemplateView.as_view()),
    path('zarik-create/',ZarikCreateApiView.as_view()),
    path('tiny/',tiny,name='tiny')
]









