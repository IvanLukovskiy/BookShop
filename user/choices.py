from django.db import models


class UserStatChoice(models.TextChoices):
    CUSTOMER = 'Cus', 'Customer'
    VENDOR = 'Ven', 'Vendor'
    ADMIN = 'Adm', 'Admin (superuser)'


class PaymentStatus(models.TextChoices):
    PAID = 'Paid', 'Оплачено'
    NOT_PAID = 'Not_paid', 'Не оплачено'
