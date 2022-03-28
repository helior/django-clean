
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from . import models
from . import views


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Example
    fields = ['id', 'name', 'created_on', 'updated_on']


class ExampleViewSet(viewsets.ModelViewSet):
  queryset = models.Example.objects.all()
  serializer_class = ExampleSerializer

router = routers.DefaultRouter()
router.register(r'examples', ExampleViewSet)

urlpatterns = [
  path('', include(router.urls))
]
