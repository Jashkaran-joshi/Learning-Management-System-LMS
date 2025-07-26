from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Dean

def add_dean(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employee_id = request.POST.get('employee_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dean_image = request.FILES.get('dean_image')

        dean = Dean.objects.create(
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            gender=gender,
            date_of_birth=date_of_birth,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            salary=salary,
            email=email,
            address=address,
            dean_image=dean_image
        )

        messages.success(request, "Dean added successfully.")
        return redirect("dean_list")

    return render(request, "deans/add-dean.html")

def dean_list(request):
    deans = Dean.objects.all()
    context = {
        'dean_list': deans
    }
    return render(request, "deans/deans.html", context)

def edit_dean(request, slug):
    dean = get_object_or_404(Dean, slug=slug)

    if request.method == "POST":
        dean.first_name = request.POST.get('first_name')
        dean.last_name = request.POST.get('last_name')
        dean.employee_id = request.POST.get('employee_id')
        dean.gender = request.POST.get('gender')
        dean.date_of_birth = request.POST.get('date_of_birth')
        dean.religion = request.POST.get('religion')
        dean.joining_date = request.POST.get('joining_date')
        dean.mobile_number = request.POST.get('mobile_number')
        dean.salary = request.POST.get('salary')
        dean.email = request.POST.get('email')
        dean.address = request.POST.get('address')

        new_image = request.FILES.get('dean_image')
        if new_image:
            dean.dean_image = new_image

        dean.save()
        messages.success(request, "Dean updated successfully.")
        return redirect("dean_list")

    return render(request, "deans/edit-dean.html", {'dean': dean})

def view_dean(request, slug):
    dean = get_object_or_404(Dean, slug=slug)
    context = {
        'dean': dean
    }
    return render(request, "deans/dean-details.html", context)

def delete_dean(request, slug):
    if request.method == "POST":
        dean = get_object_or_404(Dean, slug=slug)
        dean.delete()
        messages.success(request, "Dean deleted successfully.")
        return redirect('dean_list')
    return HttpResponseForbidden()