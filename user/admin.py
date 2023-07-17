from django.contrib import admin

from user.models import CustomUser, Order, OrderItems

admin.site.register(CustomUser)
admin.site.register(Order)
admin.site.register(OrderItems)