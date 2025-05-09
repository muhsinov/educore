from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register('teachers', TeacherViewSet, basename='teachers')

urlpatterns = router.urls