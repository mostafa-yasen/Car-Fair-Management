from django.db import models
from Employees.models import Manager
from Installments.models import MonthlyInstallment

class Branch(models.Model):
    name = models.CharField(max_length=120)
    manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE
        )
    address = models.CharField(max_length=200)
    capital_equity = models.IntegerField()
    expenses = models.IntegerField()

    def __str__(self):
        return self.name


class Notification(models.Model):
    monthlyInstallment = models.ForeignKey(MonthlyInstallment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return "%s | %s" % (self.monthlyInstallment.installment.client, self.monthlyInstallment.installment.car)