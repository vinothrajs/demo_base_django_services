from django.forms import ValidationError
from orders.models import Product, Inventory, Orders
from django.utils.translation import gettext_lazy as _


def getting_products():
    products = Product.objects.all().values()
    return products


def save_orders(*, order_no, product_id, quantity, total_amount):
    getting_product_quantity = Inventory.objects.get(product_id_id=product_id)
    available_quantity = getting_product_quantity.quantity
    if quantity > available_quantity:

        raise ValidationError(
            _(
                f"Quantity requested ({quantity}) exceeds available quantity ({available_quantity})."
            ),
            code="quantity",
        )
    else:
        order = Orders.objects.create(
            order_no=order_no,
            product_id_id=product_id,
            quantity=quantity,
            total_amount=total_amount,
        )
        return order
