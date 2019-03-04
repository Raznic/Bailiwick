from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models, forms


class DomainListView(ListView):

    model = models.Domain
    paginate_by = 10
    ordering = ['name']


class DomainDetailView(DetailView):

    model = models.Domain

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            "Name": self.object.name,
            "Registry": self.object.registry.name,
        }
        return context


class DomainCreateView(CreateView):

    model = models.Domain
    form_class = forms.DomainForm
    template_name_suffix = "_create"
    success_url = reverse_lazy('domain-list')


class DomainUpdateView(UpdateView):

    model = models.Domain
    form_class = forms.DomainForm
    template_name_suffix = "_update"


class DomainDeleteView(DeleteView):

    model = models.Domain
    template_name_suffix = "_delete"
    success_url = reverse_lazy('domain-list')
