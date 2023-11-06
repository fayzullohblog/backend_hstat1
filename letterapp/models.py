from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
MyUser=get_user_model()

class BaseModel(models.Model):
    create_date=models.DateTimeField(default=timezone.now,editable=False)  #+ 30, shanbni , yakshanbi  bulsa, dushanbiga utish kerak   
    update_date=models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

    def save(self,*args,**kwargs):
        self.update_date=timezone.now()
        super().save(*args,**kwargs)



class LetterInstruction(BaseModel):       # Ko'rstma hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   company_name=models.CharField(max_length=150)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   report_name=models.CharField(max_length=100)      # hisobat nomi
   report_date=models.DateTimeField()
   created_date_add=models.DateTimeField(default=timezone.now()+timedelta(days=30)) 

   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'


class LetterSummons(BaseModel):       # Chaqiruv hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   company_name=models.CharField(max_length=150)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 1-xatdan torib oaldi
   report_date=models.DateTimeField()    #hisobat date: hisobat nomidan oladi
   created_date_add=models.DateTimeField(default=timezone.now()+timezone.timedelta(days=5))
   


   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'


class LetterCourt(BaseModel):       # Sud hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)       # 1- yoki 2- xatdan oladi
   company_name=models.CharField(max_length=150)
   ptsh=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0,null=True,blank=True)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 2-xatdan tortib oladi
   report_date=models.DateTimeField() 
   company_own=models.CharField(max_length=50)                  

   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'


class LetterReference(BaseModel):
    letter_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    