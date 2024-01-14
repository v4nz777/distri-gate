from django.contrib import admin
from products.models import Product, OrderItem, Transaction


# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Transaction)
