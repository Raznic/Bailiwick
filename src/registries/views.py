from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models, forms


class RegistryListView(ListView):

    model = models.Registry
    paginate_by = 10
    ordering = ['name']


class RegistryDetailView(DetailView):

    model = models.Registry


class RegistryCreateView(CreateView):

    model = models.Registry
    form_class = forms.RegistryForm
    template_name_suffix = "_create"
    success_url = reverse_lazy('registry-list')


class RegistryUpdateView(UpdateView):

    model = models.Registry
    form_class = forms.RegistryForm
    template_name_suffix = "_update"


class RegistryDeleteView(DeleteView):

    model = models.Registry
    template_name_suffix = "_delete"
    success_url = reverse_lazy('registry-list')
