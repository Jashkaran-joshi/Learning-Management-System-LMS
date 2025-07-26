from django.contrib import admin
from .models import Dean

# Register your models here.

@admin.register(Dean)
class DeanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'email')
    search_fields = ('first_name', 'last_name', 'employee_id')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}