from django.urls import path
from .views import AttendanceTeacher,AttendanceTeacherDetail,AdminAttendanceDetail,AttendanceStudent,AdminAttendance


urlpatterns = [
    path('student/',AttendanceStudent.as_view(),name="student_attendance"),
    path('teacher/',AttendanceTeacher.as_view(),name="teacher_attendance"),
    path('teacher/<int:pk>/',AttendanceTeacherDetail.as_view(),name="teacher_attendance_id"),
    path('admin/',AdminAttendance.as_view(),name="admin_attendance"),
    path('admin/<int:pk>/',AdminAttendanceDetail.as_view(),name="admin_attendance_id"),
]