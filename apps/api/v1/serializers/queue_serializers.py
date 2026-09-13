from rest_framework import serializers
from queue_management.models import QueueEntry

class QueueEntrySerializer(serializers.ModelSerializer):
    patient_name=serializers.CharField(source="patient.name", read_only=True)
    doctor_name=serializers.CharField(source="doctor.name", read_only=True)
    priority_display=serializers.CharField(source="get_priority_level_display", read_only=True)
    
    class Meta:
        model=QueueEntry
        fields=[
            "id",
            "token_number",
            "patient_name",
            "doctor_name",
            "priority_level",
            "priority_display",
            "status",
            "created_at",
            "called_at",
            "completed_at",
        ]