from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Sale

class SalemodelTest(TestCase):
    def setUp(self):
        self.sale = Sale.objects.create(
            customer='Cliente Teste',
            payment_method="credit"
        )

    def test_create_sale_with_required_field(self):
        """Testa se uma venda pode ser criada com campos obrigatórios."""
        self.assertEqual(self.sale.payment_method, 'credit')
        self.assertEqual(self.sale.total, 0)
        self.assertIsNotNone(self.sale.sale_date)
