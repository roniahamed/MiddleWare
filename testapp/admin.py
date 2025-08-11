from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('user_type',)
    ordering = ('username',)
    