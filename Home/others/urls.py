from django.urls import path
from . import views

urlpatterns = [
    path("library/", views.book_list, name='book_list'),
    path("library/add/", views.add_book, name="add_book"),
    path('library/<slug:slug>/', views.view_book, name='view_book'),
    path('library/<slug:slug>/edit/', views.edit_book, name='edit_book'),
    path('library/<slug:slug>/delete/', views.delete_book, name='delete_book'),

    path("sports/", views.sport_list, name='sport_list'),
    path("sports/add/", views.add_sport, name="add_sport"),
    path('sports/<slug:slug>/', views.view_sport, name='view_sport'),
    path('sports/<slug:slug>/edit/', views.edit_sport, name='edit_sport'),
    path('sports/<slug:slug>/delete/', views.delete_sport, name='delete_sport'),
    
    path('hostels/', views.hostel_list, name='hostel_list'),
    path('hostels/add/', views.add_hostel, name='add_hostel'),
    path('hostels/<slug:slug>/edit/', views.edit_hostel, name='edit_hostel'),
    path('hostels/<slug:slug>/', views.view_hostel, name='view_hostel'),
    path('hostels/<slug:slug>/delete/', views.delete_hostel, name='delete_hostel'),

    path('transport/', views.transport_list, name='transport_list'),
    path('transport/add/', views.add_transport, name='add_transport'),
    path('transport/<str:registration_number>/edit/', views.edit_transport, name='edit_transport'),
    path('transport/<str:registration_number>/', views.view_transport, name='view_transport'),
    path('transport/<str:registration_number>/delete/', views.delete_transport, name='delete_transport'),
]