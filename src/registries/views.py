from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from . import models, forms


class RegistryListView(ListView):

    model = models.Registry


class RegistryDetailView(DetailView):

    model = models.Registry


class RegistryUpdateView(UpdateView):

    model = models.Registry
    form_class = forms.RegistryForm
    template_name_suffix = "_update"
