from django.urls import path
from api.v1.views.queue_api import doctor_queue_api
urlpatterns=[
    path("doctor/<int:doctor_id>/queue/", doctor_queue_api, name="doctor_queue_api"),
]