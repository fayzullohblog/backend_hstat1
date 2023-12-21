from django.urls import path
from .views import LetterInstructionView,ZarikCreateApiView,tiny

urlpatterns =  [
    path('get_inn/',LetterInstructionView.as_view()),
    path('zarik-create/',ZarikCreateApiView.as_view()),
    path('tiny/',tiny,name='tiny')
]









