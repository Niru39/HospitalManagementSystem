from rest_framework import serializers
from .models import Bill, Payment
from patientmanagement.serializers import PatientSerializer

class BillSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'patient', 'amount', 'date_issued', 'is_paid']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'amount_paid', 'payment_date']
