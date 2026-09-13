from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from doctors.models import Doctor
from queue_management.services import get_ordered_queue
from api.v1.serializers.queue_serializers import QueueEntrySerializer

@api_view(["GET"])
def doctor_queue_api(request, doctor_id):
    doctor=get_object_or_404(Doctor, id=doctor_id)
    queue_entries=get_ordered_queue(doctor)
    serializer=QueueEntrySerializer(queue_entries, many=True)
    return Response(serializer.data)
