from django.core.validators import MinValueValidator
from django.db import models

from books.models import Books


class User(models.Model):
    Customer = 'Cus'
    Vendor = 'Ven'
    Admin = 'Adm'
    STATUS_CHOICES = [
        (Customer, 'Customer'),
        (Vendor, 'Vendor'),
        (Admin, 'Admin (superuser)'),
    ]

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, )
    description = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='Cus')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    PAID = 'Не оплачено'
    NOT_PAID = 'Оплачено'
    STATUS_CHOICES = [
        (PAID, 'Не оплачено'),
        (NOT_PAID, 'Оплачено'),
    ]

    user_id = models.ForeignKey('User', on_delete=models.PROTECT)
    vendor_id = models.ForeignKey('User', on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS_CHOICES, default='Не оплачено')


class OrderItems(models.Model):
    items = models.ForeignKey('Books', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.DecimalField(max_digits=20, decimal_places=2,
                                      default=0.00)
