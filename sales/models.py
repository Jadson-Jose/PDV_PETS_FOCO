from django.db import models

class Sale(models.Model):
    PYMENT_METHODS = [
        ('cash', 'Dinheiro'),
        ('card', 'Cartão'),
        ('pix', 'PIX'),
    ]
    customer = models.ForeignKey("Sale Customer", verbose_name=_("Sale Customer"),  # type: ignore
                                 on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(_("Total"), max_digits=10, decimal_places=2) # type: ignore
    payment_method = models.CharField(_("Payment Method"), max_length=10, choices=PYMENT_METHODS) # type: ignore
    created_at = models.DateTimeField(_("Created At"),auto_now_add=True) # type: ignore
    

class SaleItem(models.Model):
    sale = models.ForeignKey("Sale Item", verbose_name=_("Sale Item")Sale,  # type: ignore
                             on_delete=models.CASCADE, related_name="Items")
    quantity = models.PositiveIntegerField(_("Quantity")) # type: ignore
    subtotal = models.DecimalField(_("Subtotal"), max_digits=10, decimal_places=2) # type: ignore