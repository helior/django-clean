from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from . import models
from . import serializers

class ExampleViewSet(viewsets.ModelViewSet):
  parser_classes = (MultiPartParser, FormParser)
  queryset = models.Example.objects.all()
  serializer_class = serializers.ExampleSerializer

  def post(self, request, *args, **kwargs):
    file_serializer = serializers.ExampleSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)