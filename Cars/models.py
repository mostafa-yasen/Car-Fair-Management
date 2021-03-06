# PATH: src/Cars/models.py
from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=60)
    model_name = models.CharField(max_length=50)
    model_year = models.IntegerField()
    chaisis_no = models.CharField(max_length=200)
    purchasing_price = models.IntegerField()
    selling_price = models.IntegerField()
    total_expenses = models.IntegerField(default=0)
    panal_no = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    sold = models.BooleanField(default=False)
    branch = models.ForeignKey('Branches.Branch', on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return "%s | %s | %s" % (self.brand, self.model_name, self.model_year)

    def calcExpenses(self):
        expenses = self.expense_set.all()
        for exp in expenses:
            self.total_expenses += exp.amount


class Expense(models.Model):
    amount = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return "%s | %s" % (self.amount, self.note)