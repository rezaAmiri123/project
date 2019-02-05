from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,UserManager,
                                        BaseUserManager, PermissionsMixin)


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address')
#        if not kwargs.get('username'):
#            raise ValueError('user must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
 #           username=kwargs.get('username'),
            first_name=kwargs.get('first_name', ''),
            last_name=kwargs.get('last_name', ''),
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email=email, password=password, **kwargs)
        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True
        account.save()
        return account


class Account(AbstractBaseUser, PermissionsMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True, db_index=True)
#    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
#    USERNAME_FIELDS = ['username']
    objects = AccountManager()
