from django.urls import path
from .views import EmergencyViewSet

urlpatterns = [
    path('emergency/', EmergencyViewSet.as_view({'get': 'list', 'post': 'create'}), name='emergency-list'),
    path('emergency/<int:pk>/', EmergencyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='emergency-detail'),
]
