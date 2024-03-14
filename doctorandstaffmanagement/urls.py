from django.urls import path
from .views import DoctorView, StaffView

urlpatterns = [
    path ('doctors/',DoctorView.as_view({'get':'list','post':'create'}), name = 'doctor-list'),
    path('doctors/<int:pk>/', DoctorView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'doctor-details'),
    path ('staff/',StaffView.as_view({'get':'list','post':'create'}), name = 'staff-list'),
    path('staff/<int:pk>/', StaffView.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'}) , name = 'staff-details')
]
