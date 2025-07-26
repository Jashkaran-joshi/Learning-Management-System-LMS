from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('student_dashboard/', views.student_dashboard, name='student_dashboard'), 
   path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
   path('dean_dashboard/', views.dean_dashboard, name='dean_dashboard'),
]