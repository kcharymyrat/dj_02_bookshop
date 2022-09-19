from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("shop:products", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.name}"


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Product(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, default="Unknown")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    inventory = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()
    actives = ProductManager()

    class Meta:
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("shop:product_details", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"Product #{self.id}: {self.title}. Price:${self.price}"
