from django.urls import path

from .views import products_view, product_details_views

app_name = "shop"
urlpatterns = [
    path("<slug:slug>/", products_view, name="products"),
    path("product/<slug:slug>/", product_details_views, name="product_details"),
]
