from django.contrib import admin
from .models.crm import Product, Orders, Inventory

# Register your models here.

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Inventory)
