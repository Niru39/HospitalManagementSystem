from rest_framework import serializers
from .models import Appointment
from doctorandstaffmanagement.serializers import DoctorSerializer
from doctorandstaffmanagement.models import Doctor
from patientmanagement.models import Patient
from patientmanagement.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'time', 'description']

    def create(self):
        doctor = Doctor.objects.get_or_create()
        patient = Patient.objects.get_or_create()
        appointment = Appointment.objects.create(doctor=doctor, patient=patient)
        return appointment
