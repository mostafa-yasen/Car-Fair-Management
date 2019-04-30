from django.db import models
from Branches.models import Branch

class Treasur(models.Model):
    total_cash = models.IntegerField()
    total_withdraw = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return "%s | Cash: %s | Withdraw: %s" % (self.branch, self.total_cash, self.total_withdraw)