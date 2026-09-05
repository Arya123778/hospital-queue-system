from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from queue_management.models import QueueEntry

class Appointment(models.Model):
    class Status(models.TextChoices):
        BOOKED="BOOKED", "Booked"
        CONFIRMED="CONFIRMED", "Confirmed"
        CANCELLED= "CANCELLED", "Cancelled"
        CONVERTED="CONVERTED", "Converted to Token"
    
    doctor=models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="appointments",)
    patient=models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="appointments",)
    scheduled_time=models.DateTimeField()
    status=models.CharField(max_length=20, choices=Status.choices, default=Status.BOOKED,)
    queue_entry=models.OneToOneField(QueueEntry, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointment",)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=["scheduled_time"]
    
    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.scheduled_time}"
# Create your models here.
