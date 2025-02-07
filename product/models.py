from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(
        ("Category Name"), max_length=100, unique=True)
    description = models.TextField(
        ("Category Description"), blank=True, null=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(("Product Name"), max_length=200)
    description = models.TextField(("Product Description"))
    price = models.DecimalField(
        ("Product Price"), max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField(
        ("Product Stock"), validators=[MinValueValidator(0)])
    category = models.ForeignKey("Category", verbose_name=(
        "Category"), on_delete=models.CASCADE,
        related_name="products")
    barcode = models.CharField(
        ("Barcode"), max_length=50, unique=True)

    expiration_date = models.DateField(
        ("Experation Date"), blank=True, null=True)
    created_at = models.DateTimeField(
        ("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(
        ("Updated At"), auto_now=True)

    def __str__(self):
        return self.name
