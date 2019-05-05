from django.shortcuts import render
from .models import Car, Expense
from Branches.models import Branch


def cars(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    cars = Car.objects.all()
    cars = cars.filter(branch=branch)

    cars = list(cars)

    template = "Cars/cars.html"
    context = {
        'cars': cars,
        'branch': branch,
        'count': len(cars),
        'active': 'cars'
    }

    return render(request, template, context=context)


def car_details(request, branch_id, car_id):
    branch = Branch.objects.get(pk=branch_id)
    car = branch.car_set.filter(pk=car_id).first()
    car.calcExpenses()

    expenses = car.expense_set.all()

    context = {
        'branch': branch,
        'car': car,
        'expenses': expenses,
        'active': 'cars'
    }
    template = "Cars/car-details.html"
    return render(request, template, context=context)


def expenses(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    expenses = Expense.objects.all()

    temp = []
    count = 0

    for ex in expenses:
        if ex.car.branch == branch:
            print(ex)
            temp.append(ex)
            count += ex.amount


    template = "Cars/expenses.html"
    context = {
        'branch': branch,
        'expenses': temp,
        'count': count,
        'active': 'expenses'        
    }
    return render(request, template, context=context)