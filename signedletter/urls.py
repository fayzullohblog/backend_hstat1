from django.urls import path
from .views import (
            TemplateListApiView,
            PartyUserListApiView,
            TypeLetterListApiView,
            PdfFileTemplateUnsignedListApiView,
            PdfFileTemplateUnsignedDestroyApiView,
            )
urlpatterns = [
    path('partyuser/',PartyUserListApiView.as_view()),
    path('partyuser/typeletter/',TypeLetterListApiView.as_view()),
    path('partyuser/typeletter/<int:pk>/',TemplateListApiView.as_view()),
    path('partyuser/typeletter/<int:pk>/<int:pk1>/',PdfFileTemplateUnsignedListApiView.as_view()),
    path('partyuser/typeletter/pdffiletemplate-unsigned-destroy/<int:pk>/',PdfFileTemplateUnsignedDestroyApiView.as_view()),

]

