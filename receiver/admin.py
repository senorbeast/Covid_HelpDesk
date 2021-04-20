from django.contrib import admin

# Register your models here.
from .models import Needy, Res_type, Resource

admin.site.register(Res_type)
admin.site.register(Resource)
admin.site.register(Needy)
# class YourModelAdmin(model.modelAdmin):
#     list_display = ["field_one", "field_two", "related"]
#     list_display_links = ["field_one", "related"]
