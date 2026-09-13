from django.shortcuts import render,redirect, get_object_or_404
from doctors.models import Doctor
from patients.models import Patient
from .models import QueueEntry
from .services import generate_token_number, get_ordered_queue, call_next_patient, complete_queue_entry,get_currently_serving


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
def doctor_queue_view(request, doctor_id):
    doctor=get_object_or_404(Doctor, id=doctor_id)
    queue_entries=get_ordered_queue(doctor)
    
    context={
        "doctor":doctor,
        "queue_entries":queue_entries,
    }
    return render(request, "queue_management/doctor_queue.html", context)
    
def call_next_view(request, doctor_id):
    doctor=get_object_or_404(Doctor, id=doctor_id)
    call_next_patient(doctor)
    return redirect("queue_management:doctor_queue", doctor_id=doctor.id)

def complete_entry_view(request, entry_id):
    entry=get_object_or_404(QueueEntry, id=entry_id)
    doctor_id=entry.doctor.id
    complete_queue_entry(entry)
    return redirect("queue_management: doctor_queue", doctor_id=doctor_id)

def doctor_queue_view(request, doctor_id):
    doctor=get_object_or_404(Doctor, id=doctor_id)
    queue_entries=get_ordered_queue(doctor)
    currently_serving=get_currently_serving(doctor)
    context={
        "doctor":doctor,
        "queue_entries":queue_entries,
        "currently_serving":currently_serving,
    }
    return render(request, "queue_management/doctor_queue.html", context)
    