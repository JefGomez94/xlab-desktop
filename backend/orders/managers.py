from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class AppusersManager(BaseUserManager):
    def create_user(self, usr_identification, password=None, **extra_fields):
        if not usr_identification:
            raise ValueError('El usr_identification es obligatorio')
        user = self.model(usr_identification=usr_identification, **extra_fields)
        user.usr_password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, usr_identification, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usr_identification, password, **extra_fields)
