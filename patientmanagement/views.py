from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from .models import Patient
from .serializers import PatientSerializer
from core.permissions import CustomPermission

class PatientView(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            patient = self.get_queryset().get(pk=pk)
            serializer = self.serializer_class(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=404)

    def update(self, request, pk=None):
        try:
            patient = self.get_queryset().get(pk=pk)
            serializer = self.serializer_class(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=404)

    def destroy(self, request, pk=None):
        try:
            patient = self.get_queryset().get(pk=pk)
            patient.delete()
            return Response({'message': 'Patient deleted successfully'})
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=404)
