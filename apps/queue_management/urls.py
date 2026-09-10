from django.urls import path
from . import views

app_name="queue_management"

urlpatterns=[
    path("create-token/", views.create_token_view, name="create_token"),
    path("doctor/<int:doctor_id>/queue/", views.doctor_queue_view, name="doctor_queue"),
]