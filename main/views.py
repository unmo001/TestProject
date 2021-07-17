# Create your views here.
from django.views.generic import TemplateView

from registration.models import CustomUser, Company


class MainView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        if self.request.user.headquarters_owner:
            context['franchises'] = Company.objects.filter(franchise=True)
        elif self.request.user.franchise_owner:
            context['child_welfare'] = Company.objects.filter(child_welfare_facility_flag=True)
        else:
            context['workers'] = CustomUser.objects.filter(username=self.request.user)




        return context

