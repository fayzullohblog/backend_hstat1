from django.contrib import admin
from .models import MyUser
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import MyUser


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser


class MyUserAdmin(UserAdmin):
    model = MyUser
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ['username', 'phone_number', 'user_number_litter', 'role_user', 'state']

    def save_model(self, request, obj, form, change):
        if not change:
            raw_password = form.cleaned_data.get('password1')
            obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

admin.site.register(MyUser, MyUserAdmin)

