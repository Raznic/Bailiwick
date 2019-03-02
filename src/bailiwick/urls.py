from django.contrib import admin
from django.urls import path
from registries.views import RegistryListView, RegistryDetailView, RegistryUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registries/', RegistryListView.as_view(), name='registry-list'),
    path('registries/<uuid:pk>/', RegistryDetailView.as_view(), name='registry-detail'),
    path('registries/<uuid:pk>/edit/', RegistryUpdateView.as_view(), name='registry-update'),
]
