from django.shortcuts import render, redirect
from Branches.models import Branch
from .models import Deposit, Withdraw, Treasur
from django.contrib import messages

def treasury(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    treasur = branch.treasur_set.first()
    
    if request.method == 'POST':
        process = request.POST['process']
        amount = request.POST['amount']
        notes = request.POST['notes']

        if process == 'deposit':
            deposit = Deposit(amount=amount, notes=notes, treasur=treasur)
            deposit.save()
            treasur.total_cash += int(amount)
            branch.capital_equity += int(amount)
            messages.add_message(request, messages.INFO, 'Added Deposit successfully. ' + str(deposit))

        elif process == 'withdraw':
            withdraw = Withdraw(amount=amount, notes=notes, treasur=treasur)
            withdraw.save()
            treasur.total_cash -= int(amount)
            branch.capital_equity -= int(amount)
            messages.add_message(request, messages.INFO, 'Added Withdraw successfully. ' + str(withdraw))

        return redirect('/branches/' + str(branch.pk) + '/treasury/')

    template = "Treasury/treasury.html"
    context = {
        'branch': branch,
        'active': 'treasury'
    }
    return render(request, template, context=context)