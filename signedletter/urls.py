from django.urls import path
from .views import SignedCreateApiView

urlpatterns = [
    path('signed/',SignedCreateApiView.as_view())
]