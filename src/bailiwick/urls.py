from django.contrib import admin
from django.urls import path
from registries.views import RegistryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registries/', RegistryListView.as_view(), name='registry-list'),
]
