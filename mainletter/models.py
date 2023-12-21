from django.db import models
from utils.models import BaseModel
from django.core.exceptions  import ValidationError
from django.core.validators import EmailValidator
# Create your models here.
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



# class TypeLetter(BaseModel):
#     name=models.CharField(max_length=100)
     
#     def __str__(self):
#         return self.name


# class Report(BaseModel):
#     typeletter=models.ForeignKey(TypeLetter,on_delete=models.CASCADE,related_name='createtemplate')
#     name=models.CharField(max_length=150)

#     def __str__(self):
#         return f'{str(self.typeletter)},  {self.name}'
    

# class Template(BaseModel):
#     name=models.ForeignKey(Report,on_delete=models.CASCADE,related_name='template')
#     body=models.TextField()









# 2


class TypeLetter(BaseModel):
    name=models.CharField(max_length=100)
     
    def __str__(self):
        return self.name


# class Report(BaseModel):
#     typeletter=models.ForeignKey(TypeLetter,on_delete=models.CASCADE,related_name='createtemplate')
#     name=models.CharField(max_length=150)

#     def __str__(self):
#         return f'{str(self.typeletter)},  {self.name}'
    

class Template(BaseModel):
    typeletter=models.ForeignKey(TypeLetter,on_delete=models.CASCADE,related_name='template')
    title=models.CharField(max_length=150)
    body=models.TextField()
