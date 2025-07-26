from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'teacher')
    search_fields = ('name', 'code', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('teacher',)
    prepopulated_fields = {'slug': ('name',)}