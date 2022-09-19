import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from shop.models import Product

from .cart import Cart


def cart_view(request):
    return render(request, "cart/cart_summary.html")


def cart_add_view(request):
    print("YO man")
    cart_instance = Cart(request)
    if request.method == "POST":
        print(request.POST)
        post_data = json.loads(request.body.decode("utf-8"))
        print("post-data =", post_data, type(post_data))

        product_id = int(post_data.get("product_id"))
        product_qty = int(post_data.get("product_qty"))
        product = Product.actives.filter(id=product_id).first()
        print("Product =", product)

        cart_instance.add(product, product_qty)
        cart_qty = cart_instance.product_sum()
        print("cart_qty =", cart_qty)

        response = JsonResponse({"cart_qty": cart_qty})
        print("response =", response)
        print("cart_instance =", cart_instance)
        return response
