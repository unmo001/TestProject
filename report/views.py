# Create your views here.
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from report.forms import ReportForm
from registration.models import Report


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
    success_url = reverse_lazy('report:delete')


class ReportUpdateView(UpdateView):
    template_name = 'report/report_update.html'
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report:list')
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super(ReportUpdateView, self).form_valid(form)

