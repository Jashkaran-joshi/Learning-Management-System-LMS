from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher_code', 'department', 'email', 'designation')
    search_fields = ('name', 'teacher_code', 'email', 'designation')
    list_filter = ('department',)
    prepopulated_fields = {'slug': ('name',)}