from django.db import models
from utils.models import BaseModel
from django.core.exceptions  import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()


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
        
    def __str__(self) -> str:
        return self.company_name



class TypeLetter(BaseModel):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Template(BaseModel):
    typeletter=models.ForeignKey(TypeLetter,on_delete=models.CASCADE,related_name='template')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=150)
    body=models.TextField()

    def __str__(self) -> str:
        return self.title
