from django.shortcuts import render, get_object_or_404
from .models import Client
from Branches.models import Branch

app_name = "clients"


def clients(request, branch_id):
    clients = Client.objects.all()
    branch = Branch.objects.get(pk=branch_id)
    clients = clients.filter(branch=branch)
    
    template = 'Clients/clients.html'
    context = {
        'clients': clients,
        'branch': branch,
        'active': 'clients'
        }

    return render(request, template, context=context)


def details(request, branch_id, client_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    client = branch.client_set.filter(pk=client_id).first()

    template = 'Clients/client-details.html'

    context = {
        'client': client,
        'branch': branch,
        'active': 'clients'
        }

    return render(request, template, context=context)