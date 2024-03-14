
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Staff
from .serializers import DoctorSerializer, StaffSerializer
from rest_framework.viewsets import ModelViewSet
from core.permissions import CustomPermission


class DoctorView(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            doctor = self.get_queryset().get(id=pk)
            serializer = self.serializer_class(doctor)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'})

    def update(self, request, pk=None):
        try:
            doctor = self.get_queryset().get(id=pk)
            serializer = self.serializer_class(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'})

    def destroy(self, request, pk=None):
        try:
            doctor = self.get_queryset().get(id=pk)
            doctor.delete()
            return Response({'message': 'Doctor deleted successfully'})
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'})

class StaffView(ModelViewSet):  
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [ CustomPermission]
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            staff = self.get_queryset().get(id=pk)
            serializer = self.serializer_class(staff)
            return Response(serializer.data)
        except Staff.DoesNotExist:
            return Response({'error': 'Staff not found'})

    def update(self, request, pk=None):
        try:
            staff = self.get_queryset().get(id=pk)
            serializer = self.serializer_class(staff, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Staff.DoesNotExist:
            return Response({'error': 'Staff not found'})

    def destroy(self, request, pk=None):
        try:
            staff = self.get_queryset().get(id=pk)
            staff.delete()
            return Response({'message': 'Staff deleted successfully'})
        except Staff.DoesNotExist:
            return Response({'error': 'Staff not found'})

