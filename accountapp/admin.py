from django.contrib import admin
from .models import MyUser
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import MyUser
from .forms import MyUserChangeForm,MyUserCreationForm


class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    list_display = ['username', 'phone_number', 'user_number_litter', 'role_user', 'state']

admin.site.register(MyUser, MyUserAdmin)

