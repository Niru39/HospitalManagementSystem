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

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')  
        patient_data = validated_data.pop('patient') 
        doctor, _ = Doctor.objects.get_or_create(**doctor_data) 
        patient, _ = Patient.objects.get_or_create(**patient_data)
        appointment = Appointment.objects.create(doctor=doctor, patient=patient, **validated_data)
        return appointment
