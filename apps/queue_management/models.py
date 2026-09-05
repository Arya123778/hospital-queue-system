from django.db import models
from django.conf import settings
from doctors.models import Doctor
from patients.models import Patient

class QueueEntry(models.Model):
    class Priority(models.TextChoices):
        EMERGENCY="EMERGENCY", "Emergency"
        SENIOR="SENIOR", "Senior Citizen/Disability"
        NORMAL="NORMAL", "Normal"
    
    class Status(models.TextChoices):
        WAITING="WAITING", "Waiting"
        IN_PROGRESS="IN_PROGRESS", "In Progress"
        COMPLETED="COMPLETED", "Completed"
        CANCELLED="CANCELLED", "Cancelled"
        NO_SHOW="NO_SHOW", "No Show"
    
    doctor=models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="queue_entries",)
    patient=models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="queue_entries",)
    token_number=models.PositiveBigIntegerField()
    priority_level=models.CharField(max_length=20, choices=Priority.choices, default=Priority.NORMAL,)
    status=models.CharField(max_length=20, choices=Status.choices, default=Status.WAITING,)
    created_at=models.DateTimeField(auto_now_add=True)
    called_at=models.DateTimeField(null=True, blank=True)
    completed_at=models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering=["priority_level", "created_at"]
    
    def __str__(self):
        return f"Token #{self.token_number} - {self.patient.name} - Dr. {self.doctor.name}"
    
# Create your models here.
