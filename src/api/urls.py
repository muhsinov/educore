from django.urls import path, include

urlpatterns = [
    path("user/", include("api.user.urls"), name="user"),
    path("address/", include("api.address.urls"), name="address"),
    path("attendance/", include("api.attendance.urls"), name="attendance"),
]