from django.db import models

from django.db import models

APPOINTMENT_TYPES = {
    'general': 30,
    'follow_up': 15,
    'physical_exam': 45,
    'specialist': 60
}

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()  # working hours start
    end_time = models.TimeField()    # working hours end

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    appointment_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.doctor.name} - {self.date} {self.start_time}"

