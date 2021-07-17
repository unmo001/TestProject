from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username','child_welfare_facility_owner')
