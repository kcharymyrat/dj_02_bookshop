from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "price",
        "in_stock",
        "is_active",
        "inventory",
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["in_stock", "is_active", "price", "title"]
    list_editable = ["price", "is_active", "in_stock", "inventory"]


admin.site.register(Product, ProductAdmin)
