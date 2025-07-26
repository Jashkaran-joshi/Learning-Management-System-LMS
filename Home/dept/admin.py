from django.contrib import admin
from .models import Dept

# Register your models here.

@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_of_dept', 'established_year')
    list_filter = ('established_year',)
    search_fields = ('name', 'code', 'head_of_dept')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)