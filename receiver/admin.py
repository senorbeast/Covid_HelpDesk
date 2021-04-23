
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.db import models
from django import forms
# Register your models here.
from .models import Needy, Res_type, Resource, State, City, Feedback


# ! Need to filter cities by state in Resources (only on Admin panel)
# class ResourceAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ResourceAdminForm, self).__init__(*args, **kwargs)
#         if self.instance:
#             # we're operating on an existing object, not a new one...
#             state = self.instance.country
#             cities = self.objects.filter(state_id=state)
#             self.fields["city"] = models.ChoiceField(choices=cities)


# class ResourceAdmin(admin.ModelAdmin):
#     form = ResourceAdminForm


@admin.register(Resource)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'contact_name', 'state', 'city', 'resource_name']
    list_filter = ('state', "city", 'resource_name', 'verified')
    search_fields = ['contact_name']
    #autocomplete_fields = ['city']


@admin.register(State)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']


@admin.register(City)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name',  'state']
    list_filter = ('state',)


@admin.register(Res_type)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['resource_name']
    list_display = ['id', 'resource_name', 'more_info']


@admin.register(Feedback)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['suggest']
    list_display = ['id', 'suggest', 'phone']


@admin.register(Needy)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'state', 'city', 'resource_name']
    list_filter = ('state', 'city', 'resource_name')
    search_fields = ['contact_name']
