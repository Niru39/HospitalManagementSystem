from django.db import models
from doctorandstaffmanagement.models import Doctor
from patientmanagement.models import Patient
# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    # def __str__(self):
    #     return f"Appointment with {self.doctor} on {self.date} at {self.time}"
