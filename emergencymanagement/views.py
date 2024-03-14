from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Emergency
from .serializers import EmergencySerializer

class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer

