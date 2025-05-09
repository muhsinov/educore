from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, StudentGroupViewSet

router = DefaultRouter()
router.register('', GroupViewSet, basename='group')
router.register('student', StudentGroupViewSet, basename='studentgroup')

urlpatterns = [
    path('', include(router.urls)),
]
