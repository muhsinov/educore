# TODO: Define IsTeacher, IsStudent and appropriate object-level checks


### views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Student, Teacher, Course, Group, Lesson,
    Grade, Homework, StudentHomework,
    Attendance, Payment, Address, StudentCourse
)
from .serializers import (
    StudentSerializer, TeacherSerializer, CourseSerializer,
    GroupSerializer, LessonSerializer, GradeSerializer,
    HomeworkSerializer, StudentHomeworkSerializer,
    AttendanceSerializer, PaymentSerializer,
    AddressSerializer, StudentCourseSerializer
)
from .permissions import IsAdmin  # , IsTeacher, IsStudent

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    # TODO: restrict GET list/detail to role-specific logic

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

class StudentHomeworkViewSet(viewsets.ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    permission_classes = [IsAuthenticated]


### urls.py
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    StudentViewSet, TeacherViewSet, CourseViewSet, GroupViewSet,
    LessonViewSet, GradeViewSet, HomeworkViewSet, StudentHomeworkViewSet,
    AttendanceViewSet, PaymentViewSet, AddressViewSet, StudentCourseViewSet
)

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'studenthomeworks', StudentHomeworkViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'studentcourses', StudentCourseViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

# TODO: Add filtering backends and permission logic per spec
