from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=60)
    model_name = models.CharField(max_length=50)
    model_year = models.IntegerField()
    chaisis_no = models.CharField(max_length=200)
    purchasing_price = models.IntegerField()
    selling_price = models.IntegerField()
    total_expenses = models.IntegerField()
    panal_no = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    sold = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s | %s | %s" % (self.brand, self.model_name, self.model_year)


class Expense(models.Model):
    amount = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return "%s | %s | %s" % (self.amount, self.car, self.date)