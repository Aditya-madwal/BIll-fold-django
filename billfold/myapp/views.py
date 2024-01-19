from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def walletview(request, pk) :
    w = wallets.objects.get(id = pk)

    form = transactions_form(request.POST)

    transactions_list = transactions.objects.filter(wallet = w)
    w.balance = 0
    w.income = 0
    w.expense = 0
    w.save()
    for i in transactions_list :
        if i.label == "1" and i.amount != None and w.income != None:
            w.balance += int(i.amount)
            w.income += int(i.amount)
            pass
        else :
            w.balance -= int(i.amount)
            w.expense += int(i.amount)
            pass
        w.save()
    
    balance = w.balance

    context = {
        'name' : w.name,
        'form' : form,
        'transactions' : transactions_list,
        'balance' : balance,
        'income' : w.income,
        'expense' : w.expense,
    }

    if request.method == "POST" :
        if form.is_valid() :
            # form.save()
            amount = request.POST['amount']
            label = request.POST['label']
            category = request.POST['category']
            wallet = w

            new_transaction = transactions.objects.create(amount = amount, label = label, category = category, wallet = wallet)
        return redirect(f"/wallet/{pk}")

    return render(request, 'wallet.html', context = context)

def deleteview(request, pk) :
    delete_item = transactions.objects.get(id = pk)

    if request.method == 'POST' :
        delete_item.delete()
        return redirect(walletsview)
    context = {
        "item" : delete_item,
    }
    return render(request, "delete.html", context = context)

def walletsview(request) :
    form = wallets_form(request.POST)
    w = wallets.objects.all()

    if request.method == 'POST' :
        if form.is_valid() :
            form.save()
        return redirect(walletsview)

    context = {
        'form' : form,
        'wallet_list' : w,
    }
    return render(request, 'wallets.html', context = context)

# def walletview(request, pk) :
#     w = wallets.objects.get(id = pk)
#     return render(request, "wallet.html", )
