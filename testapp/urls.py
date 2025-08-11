from django.urls import path
from .views import teacher_dashboard, student_dashboard, principal_dashboard

urlpatterns = [
    path('teacher/dashboard/', teacher_dashboard, name='teacher'),
    path('student/dashboard/', student_dashboard, name='student'),
    path('principal/dashboard', principal_dashboard, name='principal')
]
