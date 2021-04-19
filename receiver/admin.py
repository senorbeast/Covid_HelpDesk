from django.contrib import admin

# Register your models here.
from .models import Needy, Resource

admin.site.register(Needy)
admin.site.register(Resource)

# class YourModelAdmin(model.modelAdmin):
#     list_display = ["field_one", "field_two", "related"]
#     list_display_links = ["field_one", "related"]
