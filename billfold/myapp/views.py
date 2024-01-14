from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

balance = 0
income = 0
expense = 0

def homeview(request) :

    global balance
    global income
    global expense

    form = transactions_form(request.POST)

    transactions_list = transactions.objects.all()

    if request.method == "POST" :
        if form.is_valid() :
            amount = request.POST['amount']
            label = request.POST['label']
            # print(amount)
            # print(label)
            form.save()
        return redirect(homeview)
    
    print(transactions_list)
    balance = 0
    expense = 0
    income = 0
    for i in transactions_list :
        print(i.label)
        if i.label == '2' :
            expense += i.amount
            balance -= i.amount
            pass
        else :
            income += i.amount
            balance += i.amount

    context = {
        'form' : form,
        'transactions' : transactions_list,
        'balance' : balance,
        'income' : income,
        'expense' : expense,
    }

    return render(request, 'homepage.html', context = context)

def deleteview(request, pk) :
    delete_item = transactions.objects.get(id = pk)

    if request.method == 'POST' :
        delete_item.delete()
        return redirect('/')
    context = {
        "item" : delete_item,
    }
    return render(request, "delete.html", context = context)
