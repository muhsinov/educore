from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViews

router = DefaultRouter()
router.register(f"lessons", LessonViews)

urlpatterns = [
    path('', include(router.urls)),
]