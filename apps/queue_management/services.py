from django.db.models import Case, When, Value, IntegerField
from .models import QueueEntry


#define the real priority order: lower number=seen first
PRIORITY_ORDER={
    QueueEntry.Priority.EMERGENCY:0,
    QueueEntry.Priority.SENIOR: 1,
    QueueEntry.Priority.NORMAL:2,
}

def get_ordered_queue(doctor):
    """Returns a doctor's waiting queue correctly ordered by real-world priority (Emergency > Senior > Normal), and within the same priority, earliest-created first."""
    priority_case = Case(
        *[
            When(priority_level=level, then=Value(order))
            for level, order in PRIORITY_ORDER.items()
        ],
        output_field=IntegerField(),
    )
    return (
        QueueEntry.objects.filter(doctor=doctor, status=QueueEntry.Status.WAITING)
        .annotate(priority_order=priority_case)
        .order_by("priority_order", "created_at")
    )
    
def generate_token_number(doctor):
    """Generates the next token number for a doctor, resetting the count each day. Token #1 for Dr. Smith today is different from Token #1 for Dr. Smith yesterday."""
    from django.utils import timezone
    today=timezone.now().date()
    last_token=(
        QueueEntry.objects.filter(doctor=doctor, created_at__date=today)
        .order_by("token_number")
        .first()
    )
    if last_token:
        return last_token.token_number+1
    return 1

def assign_priority(queue_entry, new_priority):
    """Safely updates a queue entry's priority level. Keeping this as a function (not inline in a view) means we can add logging, notifications, or validation here later without touching view code."""
    if new_priority not in QueueEntry.Priority.values:
        raise ValueError(f"Invalid priority level: {new_priority}")
    queue_entry.priority_level=new_priority
    queue_entry.save(update_fields=["priority_level"])
    return queue_entry