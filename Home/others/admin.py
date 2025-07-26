from django.contrib import admin
from .models import Book, Sport, Hostel, Transport

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'author', 'publisher', 'genre', 'publish_date', 'language', 'number_of_copies')
    list_filter = ('genre', 'language', 'publish_date')
    search_fields = ('title', 'isbn', 'author', 'publisher')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport_type', 'number_of_players', 'origin_country', 'olympic_sport', 'popularity_rank')
    list_filter = ('sport_type', 'olympic_sport')
    search_fields = ('name', 'origin_country', 'governing_body')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostel_type', 'location', 'warden_name', 'contact_number', 'total_rooms', 'available_rooms')
    list_filter = ('hostel_type',)
    search_fields = ('name', 'location', 'warden_name')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('name', 'transport_type', 'registration_number', 'capacity', 'driver_name', 'associated_hostel')
    list_filter = ('transport_type',)
    search_fields = ('name', 'registration_number', 'driver_name', 'associated_hostel__name')
    ordering = ('name',)