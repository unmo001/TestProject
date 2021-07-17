# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from registration.models import Report, CustomUser
from report.forms import ReportForm


class ReportListView(ListView):
    template_name = 'report/report_list.html'
    model = Report

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(user=self.request.user, is_public=True).order_by('insert_time')
        return context


class ReportDraftListView(ListView):
    template_name = 'report/report_draft.html'
    model = Report

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReportDraftListView, self).get_context_data(**kwargs)
        context['drafts'] = Report.objects.filter(user=self.request.user, is_public=False).order_by('insert_time')
        return context


class ReportDetailView(DetailView):
    template_name = 'report/report_detail.html'
    model = Report
    context_object_name = 'report'


class ReportDraftDetailView(DetailView):
    template_name = 'report/report_draft_detail.html'
    model = Report

    def get_context_data(self, **kwargs):
        context = super(ReportDraftDetailView, self).get_context_data(**kwargs)
        context['drafts'] = Report.objects.filter(user=self.request.user).update(is_public=True)
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


class ReportDraftUpdateView(UpdateView):
    template_name = 'report/report_draft_update.html.html'
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report:report_draft')

    def form_valid(self, form):
        form = form.save(commit=True)
        form.user = self.request.user
        if 'done' in self.request.POST:
            form.is_public = True
            form.save()
            return redirect('report:report_draft')


class ReportCreateView(CreateView):
    template_name = 'report/report_form.html'
    form_class = ReportForm
    model = Report
    success_url = reverse_lazy('report:report_list')

    def form_valid(self, form):
        context = {'form': form}
        form = form.save(commit=False)
        form.user = self.request.user
        if 'draft' in self.request.POST:
            form.save()
            return redirect(reverse_lazy('report:report_list'))

        elif self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'report/report_confirm.html', context)
        elif self.request.POST.get('next', '') == 'back':
            return render(self.request, 'report/report_form.html', context)
        elif self.request.POST.get('next', '') == 'create':
            form.is_public = True
            form.save()
            return redirect(reverse_lazy('report:report_list'))
        else:
            return redirect(reverse_lazy('report:report_list'))




