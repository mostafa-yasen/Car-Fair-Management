from django.shortcuts import render
from .models import Car, Expense
from Branches.models import Branch


def index(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    cars = Car.objects.all()
    cars = cars.filter(branch=branch)

    template = "Cars/cars.html"
    context = {
        'cars': cars,
        'branch': branch,
    }

    return render(request, template, context=context)


def details(request, branch_id, car_id):
    branch = Branch.objects.get(pk=branch_id)
    car = branch.car_set.filter(pk=car_id).first()
    car.calcExpenses()

    context = {
        'branch': branch,
        'car': car
    }
    template = "Cars/car-details.html"
    return render(request, template, context=context)