# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, UpdateView, DetailView

from access.forms import AccessForm
from registration.models import Access


class AccessListView(ListView):
    template_name = 'access/access_list.html'
    model = Access

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AccessListView, self).get_context_data(**kwargs)
        context['accesses'] = Access.objects.all().order_by('access_time')
        return context


class AccessDetailView(DetailView):
    template_name = 'access/access_detail.html'
    model = Access

    def get_context_data(self, **kwargs):
        context = super(AccessDetailView, self).get_context_data(**kwargs)
        context['accesses'] = Access.objects.all()
        return context


class AccessDeleteView(DeleteView):
    model = Access
    template_name = 'access/access_delete.html'
    success_url = reverse_lazy('access:access_list')

    def get_context_data(self, **kwargs):
        context = super(AccessDeleteView, self).get_context_data()
        context['accesses'] = Access.objects.all()
        return context


class AccessUpdateView(UpdateView):
    template_name = 'access/access_update.html'
    model = Access
    form_class = AccessForm

    def get_success_url(self):
        return reverse('access:access_detail', kwargs={'pk': self.object.pk})
