from django.db import models
from django.utils import timezone



class BaseModel(models.Model):
    create_date=models.DateTimeField(default=timezone.now,editable=False)  #+ 30, shanbni , yakshanbi  bulsa, dushanbiga utish kerak   
    update_date=models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

    def save(self,*args,**kwargs):
        self.update_date=timezone.now()
        super().save(*args,**kwargs)
