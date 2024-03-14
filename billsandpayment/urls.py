# billing/urls.py
from django.urls import path
from .views import BillViewSet, PaymentViewSet

urlpatterns = [
    path('bills/', BillViewSet.as_view({'get': 'list', 'post': 'create'}), name='bill-list'),
    path('bills/<int:pk>/', BillViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bill-detail'),
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payment-list'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='payment-detail')
]
