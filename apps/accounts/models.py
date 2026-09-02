from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", User.Role.ADMIN)
        return super().create_superuser(username, email,password, **extra_fields)
    
    
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN", "Admin"
        DOCTOR="DOCTOR", "Doctor"
        RECEPTIONIST="RECEPTIONIST","Receptionist"
        PATIENT="PATIENT", "Patient"
    role=models.CharField(max_length=20, choices=Role.choices, default=Role.PATIENT)
    
    objects=CustomUserManager()
    def __str__(self):
        return f"{self.username} ({self.role})"
    
# Create your models here.
