from django.urls import path
from . import views

urlpatterns = [
    path("exam/", views.exam_list, name='exam_list'),
    path("exam/add/", views.add_exam, name="add_exam"),
    path('exam/<str:exam_code>/', views.view_exam, name='view_exam'),
    path('exam/<str:exam_code>/edit/', views.edit_exam, name='edit_exam'),
    path('exam/<str:exam_code>/delete/', views.delete_exam, name='delete_exam'),

    path("event/", views.event_list, name='event_list'),
    path("event/add/", views.add_event, name="add_event"),
    path('event/<str:event_code>/', views.view_event, name='view_event'),
    path('event/<str:event_code>/edit/', views.edit_event, name='edit_event'),
    path('event/<str:event_code>/delete/', views.delete_event, name='delete_event'),

    path("holiday/", views.holiday_list, name='holiday_list'),
    path("holiday/add/", views.add_holiday, name="add_holiday"),
    path('holiday/<str:holiday_code>/', views.view_holiday, name='view_holiday'),
    path('holiday/<str:holiday_code>/edit/', views.edit_holiday, name='edit_holiday'),
    path('holiday/<str:holiday_code>/delete/', views.delete_holiday, name='delete_holiday'),
]