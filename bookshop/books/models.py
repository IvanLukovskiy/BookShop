from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
