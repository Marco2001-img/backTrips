from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ClienteManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone, email, password=None, address=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            address=address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = ClienteManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"