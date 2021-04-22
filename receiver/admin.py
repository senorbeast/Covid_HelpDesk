
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Needy, Res_type, Resource, State, City, Feedback


@admin.register(Res_type, State, City, Resource, Needy, Feedback)
class ViewAdmin(ImportExportModelAdmin):
    pass
