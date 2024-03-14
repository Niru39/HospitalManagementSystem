from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from core.permissions import CustomPermission


class AppointmentView(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = ([CustomPermission, IsAuthenticated])
    
    def list(self, request):
        appointments = self.get_queryset()
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            appointment = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(appointment)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'})

    def update(self, request, pk=None):
        try:
            appointment = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(appointment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'})

    def destroy(self, request, pk=None):
        try:
            appointment = self.get_queryset().get(id=pk)
            appointment.delete()
            return Response({'message': 'Appointment deleted successfully'})
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'})
    