from django.shortcuts import redirect
from django.conf import settings 
from django.urls import resolve, Resolver404
from django.http import HttpResponseForbidden


class LoginRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):

        if request.user.is_authenticated and request.path == settings.LOGIN_REDIRECT_URL:
            user_type = getattr(request.user, 'user_type', None)

            if user_type == 'TEACHER':
                return redirect('teacher')
            elif user_type == 'STUDENT':
                return redirect('student')
            elif user_type == 'PRINCIPAL':
                return redirect('principal')
            
        return self.get_response(request)
    

class DashboardAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.role_dashboard_map={
            'teacher':'TEACHER',
            'student':'STUDENT',
            'principal':'PRINCIPAL'
        }

    def __call__(self, request):

        if not request.user.is_authenticated:
            return self.get_response(request)

        try:
            current_url_name = resolve(request.path_info).url_name
        except Resolver404:
            return self.get_response(request)

        if current_url_name in self.role_dashboard_map:
            required_role = self.role_dashboard_map[current_url_name]

            user_role = getattr(request.user, 'user_type', None)

            if user_role != required_role:
                return HttpResponseForbidden(f"Access Denied: you are logged in as a {user_role}, but this is for {required_role}s only.")
        return self.get_response(request)

