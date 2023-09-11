from rest_framework.routers import DefaultRouter
from .views import PersonViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')

urlpatterns = [
    path('api/', include(router.urls)),
]