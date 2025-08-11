from django.http import HttpResponse

def teacher_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Teacher's Dashboard, {request.user.first_name} !</h1> ")

def student_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Student's Dashboard, {request.user.first_name} !</h1> ")

def principal_dashboard(request):
    return HttpResponse(f"<h1> Welcome to the Principal's Dashboard, {request.user.first_name} !</h1> ")