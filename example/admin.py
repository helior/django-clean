from django.contrib import admin
from .models import Example

class ExampleAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_on', 'updated_on')

admin.site.register(Example, ExampleAdmin)