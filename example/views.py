from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from . import filters
from . import models
from . import serializers

class ExampleViewSet(viewsets.ModelViewSet):
  filter_backends = [DjangoFilterBackend]
  filterset_class = filters.ExampleFilter

  parser_classes = (MultiPartParser, FormParser)
  queryset = models.Example.objects.all()
  serializer_class = serializers.ExampleSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['name', 'boolField', 'created_on', 'updated_on']
  search_fields = ['name', ]
  ordering_fields = ['name', 'boolField', 'created_on', 'updated_on']
  ordering='-created_on'

  def post(self, request, *args, **kwargs):
    file_serializer = serializers.ExampleSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
