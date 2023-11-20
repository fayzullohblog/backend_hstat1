from django.contrib import admin
from .models import LetterCourt,LetterInstruction,LetterReference,LetterSummons
# Register your models here.

admin.site.register([LetterCourt,LetterInstruction,LetterReference,LetterSummons])


