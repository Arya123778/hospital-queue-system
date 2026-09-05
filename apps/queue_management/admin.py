from django.contrib import admin
from .models import QueueEntry

@admin.register(QueueEntry)
class QueueEntryAdmin(admin.ModelAdmin):
    list_display=("token_number", "patient", "doctor", "priority_level", "status", "created_at" )
    list_filter=("priority_level","status", "doctor")
# Register your models here.
