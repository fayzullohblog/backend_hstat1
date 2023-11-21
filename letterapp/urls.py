from django.urls import path
from .views import ExcelUploadAPIView

urlpatterns = [
    path('get_inn/',ExcelUploadAPIView.as_view())
]