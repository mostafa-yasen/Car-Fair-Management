from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Branch

app_name = 'Branches'

def index(request):
    branches = Branch.objects.all()

    template = 'Branches/branches.html'
    context = {'branches': branches}
    return render(request, template, context=context)


def details(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    return HttpResponse(branch)