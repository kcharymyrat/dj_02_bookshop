from django.urls import path

from .views import cart_view, cart_add_view

app_name = "cart"
urlpatterns = [
    path("", cart_view, name="cart_summary"),
    path("cart-add/", cart_add_view, name="cart_add"),
]
