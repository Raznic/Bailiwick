from django.urls import path
from . import views

urlpatterns = [
    path('', views.DomainListView.as_view(), name='domain-list'),
    path('new/', views.DomainCreateView.as_view(), name='domain-create'),
    path('<uuid:pk>/', views.DomainDetailView.as_view(), name='domain-detail'),
    path('<uuid:pk>/edit/', views.DomainUpdateView.as_view(), name='domain-update'),
    path('<uuid:pk>/delete/', views.DomainDeleteView.as_view(), name='domain-delete'),
]
