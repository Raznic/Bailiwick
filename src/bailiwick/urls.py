from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

import domains.urls
import registries.urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('registries/', include(registries.urls.urlpatterns)),
    path('domains/', include(domains.urls.urlpatterns)),
]
