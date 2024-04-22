from django import forms


class Orderform(forms.Form):
    order_no = forms.CharField(
        label="Order No",
        min_length=5,
        max_length=10,
        error_messages={"required": "please enter order no"},
    )
    product_id = forms.IntegerField(label="product name")
    quantity = forms.IntegerField(label="quantity")
    total_amount = forms.IntegerField(label="total_amount")
