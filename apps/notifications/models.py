from django.db import models
from django.conf import settings

class Notification(models.Model):
    class Channel(models.TextChoices):
        SMS="SMS", "SMS"
        EMAIL="EMAIL", "Email"
        PUSH="PUSH", "Push"
    
    class Status(models.TextChoices):
        PENDING="PENDING", "Pending"
        SENT="SENT", "Sent"
        FAILED="FAILED", "Failed"
    
    recipient=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications",)
    message=models.TextField()
    channel=models.CharField(max_length=20, choices=Channel.choices)
    status=models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING,)
    created_at=models.DateTimeField(auto_now_add=True)
    sent_at=models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering=["created_at"]
    
    def __str__(self):
        return f"{self.channel} to {self.recipient.username} - {self.status}"
# Create your models here.

