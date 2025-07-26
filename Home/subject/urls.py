from django.urls import path
from . import views

urlpatterns = [
    path("", views.subject_list, name='subject_list'),
    path("add/", views.add_subject, name="add_subject"),
    path('<str:code>/', views.view_subject, name='view_subject'),
    path('<str:code>/edit/', views.edit_subject, name='edit_subject'),
    path('<str:code>/delete/', views.delete_subject, name='delete_subject'),
]