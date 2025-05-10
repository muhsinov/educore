from django.urls import path
from .views import StudentHomeworkListCreateView, StudentHomeworkDetailView

urlpatterns = [
    path('', StudentHomeworkListCreateView.as_view()),
    path('<int:pk>/', StudentHomeworkDetailView.as_view()),
]
