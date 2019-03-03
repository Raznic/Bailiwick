from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistryListView.as_view(), name='registry-list'),
    path('new/', views.RegistryCreateView.as_view(), name='registry-create'),
    path('<uuid:pk>/', views.RegistryDetailView.as_view(), name='registry-detail'),
    path('<uuid:pk>/edit/', views.RegistryUpdateView.as_view(), name='registry-update'),
    path('<uuid:pk>/delete/', views.RegistryDeleteView.as_view(), name='registry-delete'),
]
