from django.urls import path, include

urlpatterns = [
    path("address/", include("api.address.urls"), name="address"),
    path("attendance/", include("api.attendance.urls"), name="attendance"),
    path("course/", include("api.course.urls"), name="course"),
    path("grade/", include("api.grade.urls"), name="grade"),
    path("group/", include("api.group.urls"), name="group"),
    path("homework/", include("api.homework.urls"), name="homework"),
    path("lesson/", include("api.lesson.urls"), name="lesson"),
    path("payment/", include("api.payment.urls"), name="payment"),
    path("student/", include("api.student.urls"), name="student"),
    path("teacher/", include("api.teacher.urls"), name="teacher"),
    path("user/", include("api.user.urls"), name="user"),
]