from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    age = models.IntegerField()
    driving_licence = models.CharField(max_length=25)
    notes = models.TextField()

    def __str__(self):
        return "Mr. %s %s" % (self.first_name, self.last_name)