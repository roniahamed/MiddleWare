from django.urls import path
from .views import teacher_dashboard, student_dashboard, principal_dashboard, login_view, register_view, logout_view

urlpatterns = [
    path('teacher/', teacher_dashboard, name='teacher'),
    path('student/', student_dashboard, name='student'),
    path('principal/', principal_dashboard, name='principal'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
