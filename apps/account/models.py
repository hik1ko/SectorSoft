from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()
    phone_number = models.CharField(max_length=12, unique=True)
    tg_id = models.IntegerField(unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()
