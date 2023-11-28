from django.urls import path
from .views import ExcelUploadAPIView,ZarikCreateApiView

urlpatterns =  [
    path('get_inn/',ExcelUploadAPIView.as_view()),
    path('create-get/',ZarikCreateApiView.as_view())
]









