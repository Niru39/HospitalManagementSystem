from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Inventory
from .serializers import InventorySerializer
from core.permissions import CustomPermission
from rest_framework.viewsets import ModelViewSet

class InventoryView(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def list(self, request):
        inventory_item = self.get_queryset()
        serializer = self.get_serializer(inventory_item, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            inventory_items = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(inventory_items)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            return Response({'error': 'Inventory item not found'})

    def update(self, request, pk=None):
        try:
            inventory_item = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(inventory_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Inventory.DoesNotExist:
            return Response({'error': 'Inventory item not found'})

    def destroy(self, request, pk=None):
        try:
            inventory_item = self.get_queryset().get(id=pk)
            inventory_item.delete()
            return Response({'message': 'Inventory item deleted successfully'})
        except Inventory.DoesNotExist:
            return Response({'error': 'Inventory item not found'})
