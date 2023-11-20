from django.urls import path
from .views import ExcelUploadAPIView

urlpatterns = [
    path('list-create/',ExcelUploadAPIView.as_view())
]