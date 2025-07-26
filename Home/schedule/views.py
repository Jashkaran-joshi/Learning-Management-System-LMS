from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Exam, Event, Holiday

# Exam Views
def add_exam(request):
    if request.method == "POST":
        title = request.POST.get("title")
        exam_code = request.POST.get("exam_code")
        exam_type = request.POST.get("exam_type")
        subject = request.POST.get("subject")
        teacher = request.POST.get("teacher")
        exam_date = request.POST.get("exam_date")
        duration_minutes = request.POST.get("duration_minutes")
        total_marks = request.POST.get("total_marks")
        passing_marks = request.POST.get("passing_marks")
        description = request.POST.get("description")

        Exam.objects.create(
            title=title,
            exam_code=exam_code,
            exam_type=exam_type,
            subject=subject,
            teacher=teacher,
            exam_date=exam_date,
            duration_minutes=duration_minutes,
            total_marks=total_marks,
            passing_marks=passing_marks,
            description=description,
        )

        messages.success(request, "Exam added successfully.")
        return redirect("exam_list")

    return render(request, "schedules/exam/add-exam.html")


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "schedules/exam/exams.html", {"exams": exams})


def edit_exam(request, exam_code):
    exam = get_object_or_404(Exam, exam_code=exam_code)

    if request.method == "POST":
        exam.title = request.POST.get("title")
        exam.exam_code = request.POST.get("exam_code")
        exam.exam_type = request.POST.get("exam_type")
        exam.subject = request.POST.get("subject")
        exam.teacher = request.POST.get("teacher")
        exam.exam_date = request.POST.get("exam_date")
        exam.duration_minutes = request.POST.get("duration_minutes")
        exam.total_marks = request.POST.get("total_marks")
        exam.passing_marks = request.POST.get("passing_marks")
        exam.description = request.POST.get("description")

        exam.save()
        messages.success(request, "Exam updated successfully.")
        return redirect("exam_list")

    return render(request, "schedules/exam/edit-exam.html", {"exam": exam})


def view_exam(request, exam_code):
    exam = get_object_or_404(Exam, exam_code=exam_code)
    return render(request, "schedules/exam/exam-details.html", {"exam": exam})


def delete_exam(request, exam_code):
    if request.method == "POST":
        exam = get_object_or_404(Exam, exam_code=exam_code)
        exam_title = exam.title
        exam.delete()
        messages.success(request, f"Exam '{exam_title}' deleted successfully.")
        return redirect("exam_list")
    return HttpResponseForbidden()


# Event Views
def add_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        event_code = request.POST.get("event_code")
        event_type = request.POST.get("event_type")
        department = request.POST.get("department")
        organizer = request.POST.get("organizer")
        event_date = request.POST.get("event_date")
        start_time = request.POST.get("start_time")
        duration_minutes = request.POST.get("duration_minutes")
        location = request.POST.get("location")
        description = request.POST.get("description")

        Event.objects.create(
            title=title,
            event_code=event_code,
            event_type=event_type,
            department=department,
            organizer=organizer,
            event_date=event_date,
            start_time=start_time,
            duration_minutes=duration_minutes,
            location=location,
            description=description,
        )

        messages.success(request, "Event added successfully.")
        return redirect("event_list")

    return render(request, "schedules/events/add-event.html")


def event_list(request):
    events = Event.objects.all()
    return render(request, "schedules/events/events.html", {"events": events})


def edit_event(request, event_code):
    event = get_object_or_404(Event, event_code=event_code)

    if request.method == "POST":
        event.title = request.POST.get("title")
        event.event_code = request.POST.get("event_code")
        event.event_type = request.POST.get("event_type")
        event.department = request.POST.get("department")
        event.organizer = request.POST.get("organizer")
        event.event_date = request.POST.get("event_date")
        event.start_time = request.POST.get("start_time")
        event.duration_minutes = request.POST.get("duration_minutes")
        event.location = request.POST.get("location")
        event.description = request.POST.get("description")

        event.save()
        messages.success(request, "Event updated successfully.")
        return redirect("event_list")

    return render(request, "schedules/events/edit-event.html", {"event": event})


def view_event(request, event_code):
    event = get_object_or_404(Event, event_code=event_code)
    return render(request, "schedules/events/event-details.html", {"event": event})


def delete_event(request, event_code):
    if request.method == "POST":
        event = get_object_or_404(Event, event_code=event_code)
        event_title = event.title
        event.delete()
        messages.success(request, f"Event '{event_title}' deleted successfully.")
        return redirect("event_list")
    return HttpResponseForbidden()


# holiday views
def add_holiday(request):
    if request.method == "POST":
        title = request.POST.get("title")
        holiday_code = request.POST.get("holiday_code")
        holiday_type = request.POST.get("holiday_type")
        department = request.POST.get("department")
        date = request.POST.get("date")
        description = request.POST.get("description")

        Holiday.objects.create(
            title=title,
            holiday_code=holiday_code,
            holiday_type=holiday_type,
            department=department,
            date=date,
            description=description,
        )

        messages.success(request, "Holiday added successfully.")
        return redirect("holiday_list")

    return render(request, "schedules/holidays/add-holiday.html")


def holiday_list(request):
    holidays = Holiday.objects.all().order_by("date")
    return render(request, "schedules/holidays/holidays.html", {"holidays": holidays})


def edit_holiday(request, holiday_code):
    holiday = get_object_or_404(Holiday, holiday_code=holiday_code)

    if request.method == "POST":
        holiday.title = request.POST.get("title")
        holiday.holiday_code = request.POST.get("holiday_code")
        holiday.holiday_type = request.POST.get("holiday_type")
        holiday.department = request.POST.get("department")
        holiday.date = request.POST.get("date")
        holiday.description = request.POST.get("description")

        holiday.save()
        messages.success(request, "Holiday updated successfully.")
        return redirect("holiday_list")

    return render(request, "schedules/holidays/edit-holiday.html", {"holiday": holiday})


def view_holiday(request, holiday_code):
    holiday = get_object_or_404(Holiday, holiday_code=holiday_code)
    return render(
        request, "schedules/holidays/holiday-details.html", {"holiday": holiday}
    )


def delete_holiday(request, holiday_code):
    if request.method == "POST":
        holiday = get_object_or_404(Holiday, holiday_code=holiday_code)
        holiday_title = holiday.title
        holiday.delete()
        messages.success(request, f"Holiday '{holiday_title}' deleted successfully.")
        return redirect("holiday_list")
    return HttpResponseForbidden()
