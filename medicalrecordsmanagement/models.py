# models.py
from django.db import models
from patientmanagement.models import Patient

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return f"Medical record for {self.patient} on {self.date}"
