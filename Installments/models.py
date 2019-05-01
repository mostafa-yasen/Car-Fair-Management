from django.db import models
from Cars.models import Car
from Clients.models import Client
from datetime import datetime

class Installment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    months = models.IntegerField()

    def __str__(self):
        return "%s | %s" % (self.client, self.car)


class MonthlyInstallment(models.Model):
    amount = models.IntegerField(default=5000)
    installment = models.ForeignKey(Installment, on_delete=models.CASCADE)
    installment_date = models.DateField(default=datetime.now)

    def __str__(self):
        return "%s | %s" % (self.installment, self.installment_date)