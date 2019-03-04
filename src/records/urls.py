from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.ARecordListView.as_view(), name='a-record-list'),
    path('a/new/', views.ARecordCreateView.as_view(), name='a-record-create'),
    path('a/<uuid:pk>/', views.ARecordDetailView.as_view(), name='a-record-detail'),
    path('a/<uuid:pk>/edit/', views.ARecordUpdateView.as_view(), name='a-record-update'),
    path('a/<uuid:pk>/delete/', views.ARecordDeleteView.as_view(), name='a-record-delete'),
]
