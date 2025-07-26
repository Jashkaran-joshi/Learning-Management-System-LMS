from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Teacher

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        teacher_code = request.POST.get('teacher_code')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        designation = request.POST.get('designation')
        bio = request.POST.get('bio')
        image = request.FILES.get('image') 

        Teacher.objects.create(
            name=name,
            teacher_code=teacher_code,
            department=department,
            email=email,
            phone=phone,
            designation=designation,
            bio=bio,
            image=image
        )

        messages.success(request, "Teacher added successfully.")
        return redirect("teacher_list")

    return render(request, "teachers/add-teacher.html")

def teacher_list(request):
    teachers = Teacher.objects.all().order_by('name')
    return render(request, "teachers/teachers.html", {"teachers": teachers})

def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)

    if request.method == "POST":
        teacher.name = request.POST.get('name')
        teacher.teacher_code = request.POST.get('teacher_code')
        teacher.department = request.POST.get('department')
        teacher.email = request.POST.get('email')
        teacher.phone = request.POST.get('phone')
        teacher.designation = request.POST.get('designation')
        teacher.bio = request.POST.get('bio')

        if request.FILES.get('image'):
            teacher.image = request.FILES.get('image')

        teacher.save()
        messages.success(request, "Teacher updated successfully.")
        return redirect("teacher_list")

    return render(request, "teachers/edit-teacher.html", {"teacher": teacher})

def view_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, "teachers/teacher-details.html", {"teacher": teacher})

def delete_teacher(request, slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher_name = teacher.name
        teacher.delete()
        messages.success(request, f"Teacher '{teacher_name}' deleted successfully.")
        return redirect("teacher_list")
    return HttpResponseForbidden()