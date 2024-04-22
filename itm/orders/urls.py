from django.urls import path
from . import views


urlpatterns = [
    path("", views.order_view, name="order_view"),
    path("submit_order/", views.submit_order, name="submit_order"),
]
