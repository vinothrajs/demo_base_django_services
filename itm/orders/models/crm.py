from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)

    class Meta:
        db_table = "product"


class Inventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "inventory"


class Orders(models.Model):
    order_no = models.CharField(max_length=5)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.IntegerField()

    class Meta:
        db_table = "orders"
