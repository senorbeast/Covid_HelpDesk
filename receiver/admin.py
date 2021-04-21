from django.contrib import admin

# Register your models here.
from .models import Needy, Res_type, Resource, State, City
from import_export.admin import ImportExportModelAdmin


admin.site.register(Res_type)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Resource)
admin.site.register(Needy)


class ViewAdmin(ImportExportModelAdmin):
    pass
