from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, )
    description = models.TextField()
    is_customer = models.BooleanField()
    is_staff = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


"""
Либо так:
"""


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, )
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vendor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, )
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
