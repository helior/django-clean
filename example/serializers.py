from rest_framework import serializers
from . import models

class ExampleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Example
    fields = ['id', 'name', 'image', 'created_on', 'updated_on']
