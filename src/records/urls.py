from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.ARecordListView.as_view(), name='a-record-list'),
    path('a/new/', views.ARecordCreateView.as_view(), name='a-record-create'),
    path('a/<uuid:pk>/', views.ARecordDetailView.as_view(), name='a-record-detail'),
    path('a/<uuid:pk>/edit/', views.ARecordUpdateView.as_view(), name='a-record-update'),
    path('a/<uuid:pk>/delete/', views.ARecordDeleteView.as_view(), name='a-record-delete'),
    path('ns/', views.NsRecordListView.as_view(), name='ns-record-list'),
    path('ns/new/', views.NsRecordCreateView.as_view(), name='ns-record-create'),
    path('ns/<uuid:pk>/', views.NsRecordDetailView.as_view(), name='ns-record-detail'),
    path('ns/<uuid:pk>/edit/', views.NsRecordUpdateView.as_view(), name='ns-record-update'),
    path('ns/<uuid:pk>/delete/', views.NsRecordDeleteView.as_view(), name='ns-record-delete'),
    path('mx/', views.MxRecordListView.as_view(), name='mx-record-list'),
    path('mx/new/', views.MxRecordCreateView.as_view(), name='mx-record-create'),
    path('mx/<uuid:pk>/', views.MxRecordDetailView.as_view(), name='mx-record-detail'),
    path('mx/<uuid:pk>/edit/', views.MxRecordUpdateView.as_view(), name='mx-record-update'),
    path('mx/<uuid:pk>/delete/', views.MxRecordDeleteView.as_view(), name='mx-record-delete'),
]
