from django.core.validators import MinValueValidator
from django.db import models

from books.models import Books


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, )
    description = models.TextField()
    is_customer = models.BooleanField()
    is_vendor = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Sales(models.Model):
    item_id = models.ManyToManyField('Books')
    user_id = models.ManyToManyField('User')
    vendor_id = models.ManyToManyField('User')
    amount = models.PositiveIntegerField(default=1,
                                         validators=[MinValueValidator(1)])
    sum = models.DecimalField(max_digits=20, decimal_places=2,
                              validators=[MinValueValidator(1)])
