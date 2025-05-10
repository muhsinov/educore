from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, StudentHomeworkViewSet

router = DefaultRouter()
router.register(r'', HomeworkViewSet, basename='homework')
router.register(r'submissions', StudentHomeworkViewSet, basename='student-homework')

urlpatterns = [
    path('', include(router.urls))
]