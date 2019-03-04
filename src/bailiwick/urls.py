from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('domains/', include('domains.urls')),
    path('records/', include('records.urls')),
    path('registries/', include('registries.urls')),
]
