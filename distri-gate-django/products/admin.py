from django.contrib import admin
from products.models import Product, OrderItem, Transaction, ProductVariant, Rate


# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(ProductVariant)
admin.site.register(Rate)