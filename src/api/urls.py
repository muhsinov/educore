from django.urls import path, include

urlpatterns = [
    path("user/", include("api.user.urls"), name="user"),
    path('group/', include('api.group.urls'), name='group'),
]