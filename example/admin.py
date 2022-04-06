from django.contrib import admin
from .models import Example

class ExampleAdmin(admin.ModelAdmin):
  # Iterate over sortable attributes
  list_display = ('name', 'created_on', 'updated_on')

  # Iterate over "searchable" attributes
  search_fields = ['name']

  # Iterate over "groupable" attributes
  list_filter = ['created_on']

admin.site.register(Example, ExampleAdmin)