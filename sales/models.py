from django.db import models

class Sale(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
        ('pix', 'PIX'),
    ]

    customer = models.CharField(
        ("Customer Name"), max_length=200, blank=True, null=True)
    sale_date = models.DateTimeField(
        ("Sale Date"), auto_now_add=True)
    payment_method = models.CharField(
        ("Payment Method"), max_length=50, choices=PAYMENT_METHODS, default='cash')
    total = models.DecimalField(
        ("Total"), max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Sale #{self.id} - {self.total}"