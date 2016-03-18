from django.db import models

# Create your models here.

from datetime import date

class Restaurant(models.Model):
    name = models.TextField()
    telephone = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    free = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.name



class Client(models.Model):
    name = models.TextField()
    DNI = models.CharField(max_length=9)
    age = models.IntegerField(blank=False, null=False)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.name

