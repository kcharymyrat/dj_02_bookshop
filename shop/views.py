from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def products_view(request, slug):
    if slug == "all":
        qs = Product.actives.all()
    else:
        category = get_object_or_404(Category, slug=slug)
        qs = Product.actives.filter(category=category)
    return render(request, "index.html", {"products": qs})


def product_details_views(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_details.html", {"product": product})
