from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from . import models, forms


class RegistryListView(ListView):

    model = models.Registry


class RegistryDetailView(DetailView):

    model = models.Registry


class RegistryCreateView(CreateView):

    model = models.Registry
    form_class = forms.RegistryForm
    template_name_suffix = "_create"
    success_url = "/registries/"


class RegistryUpdateView(UpdateView):

    model = models.Registry
    form_class = forms.RegistryForm
    template_name_suffix = "_update"
