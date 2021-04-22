
from django.contrib import admin

# Register your models here.
from .models import Needy, Res_type, Resource, State, City, Feedback

admin.site.register(Res_type)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Resource)
admin.site.register(Needy)
admin.site.register(Feedback)


# @admin.register(Res_type, State, City, Resource, Needy, Feedback)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
