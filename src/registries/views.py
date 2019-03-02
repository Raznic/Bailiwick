from django.views.generic.list import ListView
from . import models


class RegistryListView(ListView):

    model = models.Registry
