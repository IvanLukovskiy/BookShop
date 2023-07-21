from django.contrib.auth.models import AbstractUser
from django.db import models

from user.choices import UserStatChoice, PaymentStatus

from books.models import Books


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        blank=True,
        null=True,
        max_length=150)
    status = models.CharField(
        choices=UserStatChoice.choices,
        default=UserStatChoice.CUSTOMER
    )
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Order(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT, related_name='users')
    vendor_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT, related_name='vendors')
    payment_status = models.CharField(
        choices=PaymentStatus.choices,
        default=PaymentStatus.NOT_PAID
    )


class OrderItems(models.Model):
    items = models.ForeignKey(Books, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00
    )
