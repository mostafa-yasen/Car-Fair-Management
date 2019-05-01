from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        unique=True
        )
    address = models.CharField(max_length=300)
    age = models.IntegerField(default=20)
    salary = models.IntegerField()
    nid = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        unique=True
        )
    address = models.CharField(max_length=300)
    age = models.IntegerField(default=20)
    salary = models.IntegerField()
    nid = models.CharField(max_length=15)
    position = models.CharField(max_length=150)

    def __str__(self):
        return self.name