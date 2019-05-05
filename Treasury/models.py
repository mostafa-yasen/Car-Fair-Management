from django.db import models
from Branches.models import Branch

class Treasur(models.Model):
    total_cash = models.IntegerField(default=0)
    total_withdraw = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return "%s | Cash: %s | Withdraw: %s" % (self.branch, self.total_cash, self.total_withdraw)


class Deposit(models.Model):
    amount = models.IntegerField()
    notes = models.TextField()
    treasur = models.ForeignKey(Treasur, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "+ %s to %s" % (self.amount, self.treasur)


class Withdraw(models.Model):
    amount = models.IntegerField()
    notes = models.TextField()
    treasur = models.ForeignKey(Treasur, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "- %s from %s" % (self.amount, self.treasur)
