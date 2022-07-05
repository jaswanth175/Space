
from django.db import models


class MapsDB(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=1000, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
class UserDB(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    firstname = models.CharField(max_length=1000, null=False)
    lastname = models.CharField(max_length=1000, null=False)
    email = models.EmailField(max_length=1000,null=False)
    phone = models.CharField(max_length=1000,null=False)
    password = models.CharField(max_length=1000,null=False)


