from django.db import models
from Employees.models import Manager

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