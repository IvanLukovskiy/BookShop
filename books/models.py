from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinValueValidator




class Books(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=20, decimal_places=2,
                                validators=[MinValueValidator(0)])
    amount = models.PositiveIntegerField(default=0,
                                         validators=[MinValueValidator(0)])
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, default='None')
    middle_name = models.CharField(max_length=100, default='None')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
