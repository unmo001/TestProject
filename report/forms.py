from django import forms

from registration.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('insert_time', 'area', 'text', 'remarks',)
