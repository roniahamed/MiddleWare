from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserTypes(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        PRINCIPAL = 'PRINCIPAL', 'Principal'

    user_type = models.CharField(
        max_length=30, 
        choices=UserTypes.choices, default=UserTypes.STUDENT
    )