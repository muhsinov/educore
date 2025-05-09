from django.urls import path, include

urlpatterns = [
    path("user/", include("api.user.urls"), name="user"),
    path("course/", include("api.course.urls"), name="course"),
    path("group/", include("api.group.urls"), name="group"),
    path("lesson/", include("api.lesson.urls")),
    path("grade/", include("api.grade.urls"), name="grade"),
    path("student/", include("api.student.urls"), name="student"),

]