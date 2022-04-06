
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from . import viewsets

router = routers.DefaultRouter()

# 🔁 Iterate over models
router.register(r'examples', viewsets.ExampleViewSet)

urlpatterns = [
  path('', include(router.urls))
]
