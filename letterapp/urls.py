from django.urls import path
from .views import ExcelUploadAPIView,ZarikCreateApiView,tiny

urlpatterns =  [
    path('get_inn/',ExcelUploadAPIView.as_view()),
    path('zarik-create/',ZarikCreateApiView.as_view()),
    path('tiny/',tiny,name='tiny')
]









