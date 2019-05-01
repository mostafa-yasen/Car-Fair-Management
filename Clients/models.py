from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(default='No Address.', max_length=200)
    age = models.IntegerField()
    driving_licence = models.CharField(max_length=25)
    notes = models.TextField()
    branch = models.ForeignKey('Branches.branch', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "Mr. %s %s" % (self.first_name, self.last_name)