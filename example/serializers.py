from rest_framework import serializers
from . import models

# 🔁 Iterate over models
class ExampleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Example
    # 🔁 Iterate over none-hidden attributes
    fields = ['id', 'name', 'image', 'created_on', 'updated_on']
