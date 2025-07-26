from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Subject
from teacher.models import Teacher

def add_subject(request):
    teachers = Teacher.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        teacher_id = request.POST.get('teacher')
        description = request.POST.get('description')

        teacher = get_object_or_404(Teacher, id=teacher_id)

        Subject.objects.create(
            name=name,
            code=code,
            teacher=teacher,
            description=description
        )

        messages.success(request, "Subject added successfully.")
        return redirect("subject_list")

    return render(request, "subjects/add-subject.html", {"teachers": teachers})

def subject_list(request):
    subjects = Subject.objects.select_related('teacher').all().order_by('name')
    return render(request, "subjects/subjects.html", {"subjects": subjects})

def edit_subject(request, code):
    subject = get_object_or_404(Subject, code=code)
    teachers = Teacher.objects.all()

    if request.method == "POST":
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        teacher_id = request.POST.get('teacher')
        subject.description = request.POST.get('description')

        subject.teacher = get_object_or_404(Teacher, id=teacher_id)
        subject.save()

        messages.success(request, "Subject updated successfully.")
        return redirect("subject_list")

    return render(request, "subjects/edit-subject.html", {
        "subject": subject,
        "teachers": teachers
    })

def view_subject(request, code):
    subject = get_object_or_404(Subject, code=code)
    return render(request, "subjects/subject-details.html", {"subject": subject})

def delete_subject(request, code):
    if request.method == "POST":
        subject = get_object_or_404(Subject, code=code)
        subject_name = subject.name
        subject.delete()
        messages.success(request, f"Subject '{subject_name}' deleted successfully.")
        return redirect("subject_list")
    return HttpResponseForbidden()