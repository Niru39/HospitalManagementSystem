from django.urls import path
from .views import MedicalRecordView

urlpatterns = [
    path ('medicalrecords/',MedicalRecordView.as_view({'get':'list','post':'create'}), name = 'medicalrecords-list'),
    path('medicalrecords/<int:pk>/', MedicalRecordView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'medicalrecords-details')
]
