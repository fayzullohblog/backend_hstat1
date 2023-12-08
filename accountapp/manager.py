from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, first_name=None, last_name=None, password=None,):
        print('----->1',username,password)
        if not username:
            raise ValueError("User must have a phone number")
        if not password:
            raise ValueError("User must have a Password")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name=None, last_name=None, password=None):
        print('------>2',username,password)
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,

        )
        user.is_superuser = True
        user.save(using=self._db)
        return user