from django import forms
from .models import Resource, Needy, City, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class HelpForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['contact_name', 'email_id',
                  'phone', 'state', 'city', 'resource_name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')


class NeedForm(forms.ModelForm):
    class Meta:
        model = Needy
        fields = ['name', 'email_id', 'phone',
                  'state', 'city', 'resource_name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by(
                'name')


class FeebackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['phone', 'suggest', 'any_misconduct']


class Post_filt(forms.ModelForm):
    class Meta:
        model = Needy
        fields = ['state', 'city', 'resource_name']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     #self.fields['city'].queryset = City.objects.none()

    #     if 'state' in self.data:
    #         try:
    #             state_id = int(self.data.get('state'))
    #             self.fields['city'].queryset = City.objects.filter(
    #                 state_id=state_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.state.city_set.order_by(
    #             'name')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')