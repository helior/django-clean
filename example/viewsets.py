from rest_framework import viewsets
from . import models
from . import serializers

# 🔁 Iterate over models
class ExampleViewSet(viewsets.ModelViewSet):
  queryset = models.Example.objects.all()
  serializer_class = serializers.ExampleSerializer