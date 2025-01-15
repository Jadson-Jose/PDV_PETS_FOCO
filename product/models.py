from django.db import models

class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100, unique=True) # type: ignore
    description = models.TextField(_("Category Description"), blank=True, null=True) # type: ignore
    
    
class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=200) # type: ignore
    description = models.TextField(_("Product Description")) # type: ignore
    price = models.DecimalField(_("Product Price"), max_digits=10, decimal_places=2) # type: ignore
    stock = models.PositiveIntegerField(_("Product Stock")) # type: ignore
    category = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE, related_name="products") # type: ignore
    barcode = models.CharField(_("Barcode"), max_length=50, unique=True) # type: ignore
    expiration_date = models.DateField(_("Experation Date"), blank=True, null=True) # type: ignore # Para produtos perecíveis
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True) # type: ignore
    updated_at = models.DateTimeField(_("Updated At"), auto_now_add=True) # type: ignore
