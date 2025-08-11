from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages

def teacher_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Teacher's Dashboard, {request.user.username} !</h1> ")

def student_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Student's Dashboard, {request.user.username} !</h1> ")

def principal_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Principal's Dashboard, {request.user.username} !</h1> ")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')  # Change as needed
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, user_type=user_type)
            login(request, user)
            return redirect('/')  # Change as needed
    return render(request, 'registration.html')

def logout_view(request):
    logout(request)
    return redirect('login')