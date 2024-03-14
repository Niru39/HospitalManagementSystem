from django.urls import path
from .views import PatientView

urlpatterns = [
     path ('patient/',PatientView.as_view({'get':'list','post':'create'}), name = 'patient-list'),
    path('patient/<int:pk>/', PatientView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'patient-details')
]
