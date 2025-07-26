from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dept_list, name='dept_list'),
    path("add/", views.add_dept, name="add_dept"),
    path('<slug:slug>/', views.view_dept, name='view_dept'),
    path('<slug:slug>/edit/', views.edit_dept, name='edit_dept'),
    path('<slug:slug>/delete/', views.delete_dept, name='delete_dept'),
]