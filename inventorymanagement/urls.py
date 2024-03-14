from django.urls import path
from .views import InventoryView

urlpatterns = [
    path ('inventory/',InventoryView.as_view({'get':'list','post':'create'}), name = 'inventory items-list'),
    path('inventory/<int:pk>/', InventoryView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'inventory items-details')
]
