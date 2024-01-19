from myapp.models import *

w = wallets.objects.all()
t = transactions.objects.all()


w1 = wallets.objects.get(id = 3)
w2 = wallets.objects.get(id = 5)
w3 = wallets.objects.get(id = 6)

t.delete()

transactions.objects.create(amount = 12121, label = "1", category = "food", wallet = w1).save()
transactions.objects.create(amount = 342, label = "2", category = "food", wallet = w2).save()
transactions.objects.create(amount = 3434, label = "1", category = "food", wallet = w3).save()
transactions.objects.create(amount = 7675, label = "2", category = "food", wallet = w1).save()
transactions.objects.create(amount = 5464, label = "1", category = "food", wallet = w2).save()
transactions.objects.create(amount = 343, label = "2", category = "food", wallet = w3).save()
transactions.objects.create(amount = 454, label = "1", category = "food", wallet = w1).save()
transactions.objects.create(amount = 7745, label = "2", category = "food", wallet = w2).save()
transactions.objects.create(amount = 5567, label = "1", category = "food", wallet = w3).save()
transactions.objects.create(amount = 231, label = "1", category = "food", wallet = w1).save()
transactions.objects.create(amount = 87987, label = "2", category = "food", wallet = w2).save()
transactions.objects.create(amount = 676, label = "1", category = "food", wallet = w1).save()
transactions.objects.create(amount = 656, label = "2", category = "food", wallet = w3).save()
transactions.objects.create(amount = 9909, label = "1", category = "food", wallet = w3).save()
transactions.objects.create(amount = 546, label = "2", category = "food", wallet = w2).save()
transactions.objects.create(amount = 23, label = "1", category = "food", wallet = w1).save()
transactions.objects.create(amount = 343, label = "2", category = "food", wallet = w2).save()
transactions.objects.create(amount = 645, label = "1", category = "food", wallet = w3).save()

print("---------------------------")
print(transactions.objects.filter(wallet = w1))
print("---------------------------")
print("---------------------------")
print(transactions.objects.filter(wallet = w2))
print("---------------------------")
print("---------------------------")
print(transactions.objects.filter(wallet = w3))
print("---------------------------")



print(w)
print(t)
