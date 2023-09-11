from rest_framework.routers import DefaultRouter
from .views import PersonViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', PersonViewSet, basename='person')

urlpatterns = router.urls