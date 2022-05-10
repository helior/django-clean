
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# 🔁 Iterate over models
router.register(r'examples', views.ExampleViewSet)

urlpatterns = [
  path('', include(router.urls))
]
