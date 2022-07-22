from rest_framework import serializers
from . import models

# 🔁 Iterate over models
class ExampleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Example
    # 🔁 Iterate over none-hidden attributes
    fields = ['id', 'name', 'value', 'isGoodExample', 'image', 'created_on', 'updated_on']
