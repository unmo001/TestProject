from django import forms

from registration.models import Access


class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ('user_name', 'access_time', 'leave_time')
