from django.contrib import admin
from .models import Exam, Event, Holiday

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'exam_code', 'exam_type', 'subject', 'teacher', 'exam_date', 'total_marks', 'passing_marks')
    list_filter = ('exam_type', 'subject', 'exam_date')
    search_fields = ('title', 'exam_code', 'subject', 'teacher')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('exam_date',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_code', 'event_type', 'department', 'organizer', 'event_date', 'start_time', 'location')
    list_filter = ('event_type', 'department', 'event_date')
    search_fields = ('title', 'event_code', 'organizer', 'location')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('event_date',)

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'holiday_code', 'holiday_type', 'department', 'date')
    list_filter = ('holiday_type', 'department', 'date')
    search_fields = ('title', 'holiday_code')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('date',)