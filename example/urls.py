
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from . import models

# 🔁 Iterate over models
class ExampleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Example
    # 🔁 Iterate over none-hidden attributes
    fields = ['id', 'name', 'created_on', 'updated_on']

# 🔁 Iterate over models
class ExampleViewSet(viewsets.ModelViewSet):
  queryset = models.Example.objects.all()
  serializer_class = ExampleSerializer


router = routers.DefaultRouter()

# 🔁 Iterate over models
router.register(r'examples', ExampleViewSet)

urlpatterns = [
  path('', include(router.urls))
]
