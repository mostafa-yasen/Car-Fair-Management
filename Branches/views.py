from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch


def index(request):
    branches = Branch.objects.all()

    template = 'Branches/branches.html'
    context = {'branches': branches}
    return render(request, template, context=context)