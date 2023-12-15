from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions  import ValidationError
from django.core.validators import EmailValidator
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


class Zarik(BaseModel):
    
    company_name=models.CharField(max_length=300)

    adress=models.CharField(max_length=300)
    street=models.CharField(max_length=300)


    phone_number=models.CharField(max_length=50)
    inn_number=models.CharField(max_length=50)

    email=models.EmailField(validators=[EmailValidator()])
    soato=models.CharField(max_length=50)

    def clean(self):
        if not (self.phone_number or self.email):
            raise ValidationError("At least one of phone number or email is required.")



class ReportCategory(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class LetterInstruction(BaseModel):       # Ko'rstma hati
   
   report_category=models.ForeignKey(ReportCategory,on_delete=models.PROTECT,related_name='letterinstructuion')
   letter_name=models.CharField(max_length=100)      # hisobat nomi
   company_name=models.CharField(max_length=150)

   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   
   
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   
   litter_number=models.CharField(max_length=15)
   inn_number=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   soato=models.CharField(max_length=50)
   
   report_date=models.DateTimeField(auto_now=True)
   created_date_add=models.DateTimeField(default=timezone.now()+timedelta(days=30)) 

   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])

   def __repr__(self) -> str:
          return self.letter_name 
        
    #FIXME: keyingisafar bundan foydalanmayman


class LetterSummons(BaseModel):# Chaqiruv hati

   
   letter_name=models.CharField(max_length=50)
   company_name=models.CharField(max_length=150)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 1-xatdan torib oaldi
   
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True)

   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   
   litter_number=models.CharField(unique=True,max_length=15)
   inn_number=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   
   report_date=models.DateTimeField()    #hisobat date: hisobat nomidan oladi
   created_date_add=models.DateTimeField(default=timezone.now()+timezone.timedelta(days=5))

   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])


   


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
    