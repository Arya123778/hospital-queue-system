from django.shortcuts import render,redirect, get_object_or_404
from doctors.models import Doctor
from patients.models import Patient
from .models import QueueEntry
from .services import generate_token_number

def create_token_view(request):
    doctors=Doctor.objects.filter(is_available=True)
    patients=Patient.objects.all()
    
    if request.method=="POST":
        doctor=get_object_or_404(Doctor, id=request.POST.get("doctor_id"))
        patient=get_object_or_404(Patient, id=request.POST.get("patient_id"))
        priority=request.POST.get("priority_level", QueueEntry.Priority.NORMAL)
        
        token_number=generate_token_number(doctor)
        
        QueueEntry.objects.create(
            doctor=doctor,
            patient=patient,
            token_number=token_number,
            priority_level=priority,
        )
        
        return redirect("queue_management:create_token")
    
    context={
        "doctors":doctors,
        "patients": patients,
        "priority_choices":QueueEntry.Priority.choices,
    }
    return render(request, "queue_management/create_token.html", context)

# Create your views here.
