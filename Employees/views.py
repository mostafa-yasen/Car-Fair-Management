from django.shortcuts import render
from .models import Manager, Employee
from Branches.models import Branch


def employees(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    manager = branch.manager_set.first()
    employees = list(branch.employee_set.all())
    count = len(employees)


    template = "Employees/employees.html"
    context = {
        'branch': branch,
        'manager': manager,
        'employees': employees,
        'count': count,
        'active': 'employees'
    }

    return render(request, template, context=context)


def emp_details(request, branch_id, employee_id):
    branch = Branch.objects.get(pk=branch_id)
    employee = branch.employee_set.filter(pk=employee_id).first()

    template = "Employees/employee_details.html"
    context = {
        'branch': branch,
        'employee': employee,
        'active': 'employees'
    }

    return render(request, template, context=context)