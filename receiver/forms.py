from django import forms
from .models import Resource, Needy


class HelpForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['contact_name', 'email_id', 'phone', 'state', 'description']


class NeedForm(forms.ModelForm):
    class Meta:
        model = Needy
        fields = ['name', 'email_id', 'phone',
                  'state', 'description']
