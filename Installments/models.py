from django.db import models
from Cars.models import Car
from Clients.models import Client

class Installment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    months = models.IntegerField()

    def __str__(self):
        return "%s | %s" % (self.client, self.car)
