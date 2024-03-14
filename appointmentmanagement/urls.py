from django.urls import path
from .views import AppointmentView

urlpatterns = [
    path ('appointment/',AppointmentView.as_view({'get':'list','post':'create'}), name = 'appointment-list'),
    path('appointment/<int:pk>/', AppointmentView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'appointment-details')
]
