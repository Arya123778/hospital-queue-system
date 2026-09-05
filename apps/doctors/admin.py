from django.contrib import admin
from .models import Doctor, ShiftSchedule

class ShiftScheduleInline(admin.TabularInline):
    model=ShiftSchedule
    extra=1

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=("name", "specialization", "is_available", "is_queue_paused")
    inlines=[ShiftScheduleInline]
    
# Register your models here.
