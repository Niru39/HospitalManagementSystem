from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from rest_framework.response import Response
from core.permissions import CustomPermission

class MedicalRecordView(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def list(self, request):
        medical_records = self.get_queryset()
        serializer = self.get_serializer(medical_records, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            medical_record = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(medical_record)
            return Response(serializer.data)
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'})

    def update(self, request, pk=None):
        try:
            medical_record = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(medical_record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'})

    def destroy(self, request, pk=None):
        try:
            medical_record = self.get_queryset().get(id=pk)
            medical_record.delete()
            return Response({'message': 'Medical record deleted successfully'})
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'})
