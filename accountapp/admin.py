# from django.contrib import admin
# from .models import MyUser
# # Register your models here.

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm,UserCreationForm
# from .models import MyUser
# from .forms import MyUserChangeForm,MyUserCreationForm


# class MyUserAdmin(admin.ModelAdmin):
#     model = MyUser
#     list_display = ['username', 'phone_number', 'user_number_litter', 'role_user', 'state']

# admin.site.register(MyUser, MyUserAdmin)

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import MyUser

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username','is_superuser','is_staff',"is_admin",'is_active']
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["password",'username',]}),
        ("Personal info", {"fields": ["first_name",'last_name','phone_number']}),
        ("Permissions", {"fields": ["is_admin",'is_active','is_superuser','is_staff']}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "password1", "password2",'is_active'],
            },
        ),
    ]
    search_fields = ["user_number_litter"]
    ordering = ["user_number_litter"]
    filter_horizontal = []
    list_editable=["is_admin",'is_active','is_superuser',]

    # def changed_fields(self, obj):
    #     if obj.is_admin:
    #         delta = obj.is_admin(obj.is_admin)
    #         return delta.is_admin
    #     return None


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
