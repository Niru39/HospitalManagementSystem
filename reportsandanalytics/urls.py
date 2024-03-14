# urls.py
from django.urls import path
from .views import ReportViewSet

urlpatterns = [
    path('reports/', ReportViewSet.as_view({'get': 'list',  'post': 'create'}), name='report-list'),
    path('reports/<int:pk>/', ReportViewSet.as_view({'get': 'retrieve',  'put': 'update', 'delete': 'destroy' }), name='report-detail'),
]
