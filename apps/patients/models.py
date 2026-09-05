from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE="MALE", "Male"
        FEMALE="FEMALE", "Female"
        OTHER="OTHER", "Other"
    
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_profile")
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10, choices=Gender.choices)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name