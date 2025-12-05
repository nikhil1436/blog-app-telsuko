from django.urls import path
from . import views

urlpatterns = [
    path('doctors/<int:doctor_id>/schedule/', views.doctor_schedule),
    path('doctors/<int:doctor_id>/available-slots/', views.available_slots),
    path('appointments/', views.create_appointment),
]
