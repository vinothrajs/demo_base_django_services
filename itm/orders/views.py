from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from django.views.decorators.csrf import csrf_protect

from .form import Orderform
from .services.orders import getting_products, save_orders
from django.core.exceptions import ValidationError


# Create your views here.
@require_http_methods(["GET"])
@csrf_protect
def order_view(request):

    form = Orderform()
    products = getting_products()
    return render(request, "order.html", {"form": form, "products": products})


@require_http_methods(["POST"])
@csrf_protect
def submit_order(request):
    form = Orderform(request.POST)
    if form.is_valid():  # non fucnational valdiation
        order_no = form.cleaned_data["order_no"]
        product_id = form.cleaned_data["product_id"]
        quantity = form.cleaned_data["quantity"]
        total_amount = form.cleaned_data["total_amount"]
        try:
            save_orders(
                order_no=order_no,
                product_id=product_id,
                quantity=quantity,
                total_amount=total_amount,
            )

            return JsonResponse(
                {"success": True, "message": "Order processed successfully."}
            )
        except ValidationError as e:
            errors = {e.code: [{"message": e.message}]}
            return JsonResponse({"success": False, "errors": errors})

    else:
        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        print(errors)
        return JsonResponse({"success": False, "errors": errors})
