from django.urls import path
from . import views

urlpatterns = [
    path("", views.dean_list, name='dean_list'),
    path("add/", views.add_dean, name="add_dean"),
    path('<slug:slug>/', views.view_dean, name='view_dean'),
    path('<slug:slug>/edit/', views.edit_dean, name='edit_dean'),
    path('<slug:slug>/delete/', views.delete_dean, name='delete_dean'),
]