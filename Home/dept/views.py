from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Dept

def add_dept(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        head_of_dept = request.POST.get('head_of_dept')
        established_year = request.POST.get('established_year')
        description = request.POST.get('description')

        Dept.objects.create(
            name=name,
            code=code,
            head_of_dept=head_of_dept,
            established_year=established_year if established_year else None,
            description=description
        )

        messages.success(request, "Department added successfully.")
        return redirect('dept_list')

    return render(request, "depts/add-dept.html")

def dept_list(request):
    depts = Dept.objects.all()
    context = {
        'depts': depts,
    }
    return render(request, "depts/depts.html", context)

def edit_dept(request, slug):
    dept = get_object_or_404(Dept, slug=slug)

    if request.method == "POST":
        dept.name = request.POST.get('name')
        dept.code = request.POST.get('code')
        dept.head_of_dept = request.POST.get('head_of_dept')
        dept.established_year = request.POST.get('established_year')
        dept.description = request.POST.get('description')
        dept.save()

        messages.success(request, "Department updated successfully.")
        return redirect('dept_list')

    return render(request, "depts/edit-dept.html", {'dept': dept})

def view_dept(request, slug):
    depts = get_object_or_404(Dept, slug=slug)
    return render(request, "depts/dept-details.html", {'dept': depts})

def delete_dept(request, slug):
    if request.method == "POST":
        dept = get_object_or_404(Dept, slug=slug)
        dept_name = dept.name
        dept.delete()
        messages.success(request, f"Deleted dept: {dept_name}")
        return redirect('dept_list')

    return HttpResponseForbidden()