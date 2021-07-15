# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from registration.models import Report
from report.forms import ReportForm


class ReportListView(ListView):
    template_name = 'report/report_list.html'
    model = Report

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.all().order_by('insert_time')
        return context


class ReportDetailView(DetailView):
    template_name = 'report/report_detail.html'
    model = Report

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.all()
        return context


class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'report/report_delete.html'
    success_url = reverse_lazy('report:report_list')

    def get_context_data(self, **kwargs):
        context = super(ReportDeleteView, self).get_context_data()
        context['reports'] = Report.objects.filter(user=self.kwargs['pk'])
        return context


class ReportUpdateView(UpdateView):
    template_name = 'report/report_update.html'
    model = Report
    form_class = ReportForm

    def get_success_url(self):
        return reverse('report:report_detail', kwargs={'pk': self.object.pk})


