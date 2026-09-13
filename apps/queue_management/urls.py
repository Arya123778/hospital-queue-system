from django.urls import path
from . import views

app_name="queue_management"

urlpatterns=[
    path("create-token/", views.create_token_view, name="create_token"),
    path("doctor/<int:doctor_id>/queue/", views.doctor_queue_view, name="doctor_queue"),
    path("doctor/<int:doctor_id>/call-next/", views.call_next_view, name="call_next"),
    path("entry/<int:entry_id>/complete/", views.complete_entry_view, name="complete_entry"),
]