from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from incident.form.incident_form import IncidentForm
from incident.models import Incident
from django.contrib.auth.mixins import LoginRequiredMixin


class AddIncident(LoginRequiredMixin, CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident/add_incident.html'

    def get_success_url(self):
        return reverse('incident_list', kwargs={})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'action': 'add'})
        return kwargs


class UpdateIncident(LoginRequiredMixin, UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident/update_incident.html'

    def get_success_url(self):
        return reverse('incident_list', kwargs={})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'action': 'edit'})
        kwargs.update({'user': self.request.user})
        return kwargs


class IncidentList(LoginRequiredMixin, ListView):
    context_object_name = 'incidents'
    template_name = 'incident/incident_list.html'

    def get_queryset(self):
        x = Incident.objects.filter(reporter_name=self.request.user).order_by('-report_date')
        for i in x:
            print(i)
        return Incident.objects.filter(reporter_name=self.request.user).order_by('-report_date')
