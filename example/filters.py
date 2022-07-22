from django_filters import rest_framework as filters
from . import models

class ExampleFilter(filters.filterset.FilterSet):
  value__gt = filters.NumberFilter(field_name='value', lookup_expr='gt')
  value__gte = filters.NumberFilter(field_name='value', lookup_expr='gte')
  value__lt = filters.NumberFilter(field_name='value', lookup_expr='lt')
  value__lte = filters.NumberFilter(field_name='value', lookup_expr='lte')
  value__range = filters.NumericRangeFilter()

  class Meta:
    model = models.Example
    fields = ['name', 'value', 'isGoodExample', 'created_on', 'updated_on']

  