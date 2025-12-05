from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .models import Doctor, Appointment, APPOINTMENT_TYPES
from .serializers import AppointmentSerializer, DoctorSerializer
from .utils import generate_slots

@api_view(['GET'])
def doctor_schedule(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor)
    return Response({
        "doctor": DoctorSerializer(doctor).data,
        "appointments": list(appointments.values())
    })

@api_view(['GET'])
def available_slots(request, doctor_id):
    date = request.GET.get("date")
    appointment_type = request.GET.get("appointment_type")

    duration = APPOINTMENT_TYPES.get(appointment_type)
    if not duration:
        return Response({"error": "Invalid appointment type"}, status=400)

    doctor = Doctor.objects.get(id=doctor_id)
    booked = Appointment.objects.filter(doctor=doctor, date=date)

    slots = generate_slots(doctor.start_time, doctor.end_time, booked, duration)
    return Response({"available_slots": slots})

@api_view(['POST'])
def create_appointment(request):
    data = request.data
    # basic validation:
    required = ("doctor", "date", "start_time", "appointment_type")
    for r in required:
        if r not in data:
            return Response({"error": f"{r} is required"}, status=400)

    try:
        doctor = Doctor.objects.get(id=data["doctor"])
    except Doctor.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=404)

    if data["appointment_type"] not in APPOINTMENT_TYPES:
        return Response({"error": "Invalid appointment type"}, status=400)

    duration = APPOINTMENT_TYPES[data["appointment_type"]]
    start_time = datetime.strptime(data["start_time"], "%H:%M").time()
    end_time = (
        datetime.combine(datetime.today(), start_time)
        + timedelta(minutes=duration)
    ).time()

    # overlap check
    booked = Appointment.objects.filter(doctor=doctor, date=data["date"])
    for b in booked:
        if not (end_time <= b.start_time or start_time >= b.end_time):
            return Response({"error": "Slot not available"}, status=400)

    appointment = Appointment.objects.create(
        doctor=doctor,
        date=data["date"],
        start_time=start_time,
        end_time=end_time,
        appointment_type=data["appointment_type"]
    )
    return Response(AppointmentSerializer(appointment).data)

