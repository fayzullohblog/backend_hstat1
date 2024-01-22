from django.urls import path
from .views import TemplateListApiView,PartyUserListApiView,TypeLetterListApiView

urlpatterns = [
    path('partyuser/',PartyUserListApiView.as_view()),
    path('partyuser/typeletter/',TypeLetterListApiView.as_view()),
    path('partyuser/typeletter/<int:pk>/',TemplateListApiView.as_view()),

]

