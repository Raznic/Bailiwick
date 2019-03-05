from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models, forms


class ARecordListView(ListView):

    model = models.ARecord
    paginate_by = 10
    ordering = ['hostname', 'domain', 'address']
    template_name = "records/a_record_list.html"


class ARecordDetailView(DetailView):

    model = models.ARecord
    template_name = "records/a_record_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            "Hostname": self.object.hostname,
            "Address": self.object.address,
            "Domain": self.object.domain.name,
            "Time-to-live": self.object.time_to_live,
        }
        return context


class ARecordCreateView(CreateView):

    model = models.ARecord
    form_class = forms.ARecordForm
    template_name = "records/a_record_create.html"
    success_url = reverse_lazy('a-record-list')


class ARecordUpdateView(UpdateView):

    model = models.ARecord
    form_class = forms.ARecordForm
    template_name = "records/a_record_update.html"


class ARecordDeleteView(DeleteView):

    model = models.ARecord
    template_name = "records/a_record_delete.html"
    success_url = reverse_lazy('a-record-list')


class NsRecordListView(ListView):

    model = models.NsRecord
    paginate_by = 10
    ordering = ['domain', 'name_server', 'owner']
    template_name = "records/ns_record_list.html"


class NsRecordDetailView(DetailView):

    model = models.NsRecord
    template_name = "records/ns_record_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            "Name Server": self.object.name_server,
            "Domain": self.object.domain.name,
            "Owner": self.object.owner,
            "Time-to-live": self.object.time_to_live,
        }
        return context


class NsRecordCreateView(CreateView):

    model = models.NsRecord
    form_class = forms.NsRecordForm
    template_name = "records/ns_record_create.html"
    success_url = reverse_lazy('ns-record-list')


class NsRecordUpdateView(UpdateView):

    model = models.NsRecord
    form_class = forms.NsRecordForm
    template_name = "records/ns_record_update.html"


class NsRecordDeleteView(DeleteView):

    model = models.NsRecord
    template_name = "records/ns_record_delete.html"
    success_url = reverse_lazy('ns-record-list')
