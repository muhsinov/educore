from django.urls import path
from .views import AddressteacherApiView,AddressStudentDetail,allAddressApiview,AddressDetailAdmin

urlpatterns = [
    path("student/",AddressStudentDetail.as_view(),name="student_address_id"),
    path("teacher/",AddressteacherApiView.as_view(),name="teacher_address"),
    path("admin/",allAddressApiview.as_view(),name="all_address"),
    path("admin/<int:pk>/",AddressDetailAdmin.as_view(),name="address_id"),

]