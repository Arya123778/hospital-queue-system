from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_profile",)
    name=models.CharField(max_length=150)
    specialization=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    is_queue_paused=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class ShiftSchedule(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY= "MON", "Monday"
        TUESDAY= "TUE", "Tuesday"
        WEDNESDAY="WED", "Wednesday"
        THURSDAY="THU", "Thursday"
        FRIDAY="FRI", "Friday"
        SATURDAY="SAT", "Saturday"
        SUNDAY="SUN", "Sunday"
        
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="shifts",)
    day_of_week=models.CharField(max_length=3, choices=DayOfWeek.choices)
    start_time=models.TimeField()
    end_time=models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week} ({self.start_time}-{self.end_time})"