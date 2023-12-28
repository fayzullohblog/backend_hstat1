from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta
from utils.models import BaseModel
from mainletter.models import Template,TypeLetter
# Create your models here.
MyUser=get_user_model()



class LetterInstruction(BaseModel):       # Ko'rstma hati
   
   template=models.ForeignKey(Template,on_delete=models.PROTECT,related_name='letterinstructuion')
   
   company_name=models.CharField(max_length=150)
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   
   inn_number=models.CharField(max_length=15)
   litter_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   soato=models.CharField(max_length=50)

   email=models.EmailField(null=True,blank=True)
   
   report_date=models.DateTimeField(auto_now=True)
   created_date_add=models.DateTimeField(default=timezone.now()+timedelta(days=30)) 

   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])


        
    #FIXME: keyingisafar bundan foydalanmayman


class LetterReference(BaseModel):
    letter_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    