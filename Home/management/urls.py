from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("add_expenses/", views.add_expenses, name="add_expenses"),
    path("add_fees/", views.add_fees, name="add_fees"),
    path("add_salary/", views.add_salary, name="add_salary"),
    path("expenses/", views.expenses, name="expenses"),
    path("fees/", views.fees, name="fees"),
    path("fees_collection/", views.fees_collection, name="fees_collection"),
    path("salary/", views.salary, name="salary")
]