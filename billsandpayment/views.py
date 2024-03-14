from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Bill, Payment
from .serializers import BillSerializer, PaymentSerializer
from core.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = ([CustomPermission, IsAuthenticated])
    
    def list(self, request):
        bills = self.get_queryset()
        serializer = self.get_serializer(bills, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            bill = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(bill)
            return Response(serializer.data)
        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'})

    def update(self, request, pk=None):
        try:
            bill = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'})

    def destroy(self, request, pk=None):
        try:
            bill = self.get_queryset().get(id=pk)
            bill.delete()
            return Response({'message': 'Bill deleted successfully'})
        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'})
    

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = ([CustomPermission, IsAuthenticated])


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bill_id = request.data.get('bill')
        bill = Bill.objects.get(pk=bill_id)
        if not bill.is_paid:
            payment = serializer.save()
            bill.is_paid = True
            bill.save()
            return Response({'message': 'Payment successful', 'payment_id': payment.id})
        else:
            return Response({'error': 'Bill already paid'})
