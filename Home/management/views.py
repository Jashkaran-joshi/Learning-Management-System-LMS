from django.shortcuts import render

# Create your views here.

def add_expenses(request):
    return render(request, "managements/addExpenses.html")

def add_fees(request):
    return render(request, "managements/addFees.html")

def add_salary(request):
    return render(request, "managements/addSalary.html")

def expenses(request):
    return render(request, "managements/expenses.html")

def fees(request):
    return render(request, "managements/fees.html")

def fees_collection(request):
    return render(request, "managements/feesCollection.html")

def salary(request):
    return render(request, "managements/salary.html")