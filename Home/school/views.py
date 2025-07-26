from django.shortcuts import render

def index(request):
    return render(request, "authentication/login.html")

def student_dashboard(request):
    return render(request, "students/student-dashboard.html")

def teacher_dashboard(request):
    return render(request, "teachers/teacher-dashboard.html")

def dean_dashboard(request):
    return render(request, "deans/dean-dashboard.html")