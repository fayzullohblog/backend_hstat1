from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta
from utils.models import BaseModel
from mainletter.models import Template,TypeLetter
# Create your models here.
MyUser=get_user_model()


# Upload pdf file for LetterInstruction
class PdfFilePath(models.TextChoices):
    pdf_instraction_path='pdfletterinstruction/unsigned/'

# Manager Count Class for Pdf file fields
class PdfFileLetterinstructionManager(models.Manager):
    def pdf_file_count(self):
        return self.values('pdf_file').count()


class LetterInstruction(BaseModel):       # Ko'rstma hati1
   
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
   letter_date=models.DateTimeField(default=timezone.now().date()+timedelta(days=7)) 

   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])

#    pdf_file=models.FileField(upload_to=PdfFilePath.pdf_instraction_path)


   
         
   #FIXME: keyingisafar bundan foydalanmayman



class PdfFileTemplate(BaseModel):
   
   template=models.ForeignKey(Template,on_delete=models.CASCADE,related_name='pdffiletemplate')
   pdf_file=models.FileField(upload_to=PdfFilePath.pdf_instraction_path)
   letter_date=models.DateTimeField(default=timezone.now()+timedelta(days=7))
   inn_number=models.CharField(max_length=15) 
   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])
   soato=models.CharField(max_length=50)

   objects=PdfFileLetterinstructionManager()


   def letter_date(self):
       date=self.template.update_date
       return date