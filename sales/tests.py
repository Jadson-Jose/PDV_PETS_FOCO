from django.test import TestCase
from .models import Sale
from django.core.exceptions import ValidationError

class SalemodelTest(TestCase):
    
    def test_create_sale_defaults(self):
        """Testa a criação de uma venda com valores padrão."""
        sale = Sale.objects.create()
        self.assertIsNotNone(sale.id)
        self.assertEqual(sale.payment_method, 'cash')
        self.assertEqual(sale.total, 0)

    def test_create_sale_with_custom_values(self):
        """Testa a criação de uma venda com valores personalizados"""
        sale = Sale.objects.create(
            customer="Jadson Silva",
            payment_method="credit",
            total=150.15
        )
        self.assertEqual(sale.customer, "Jadson Silva")
        self.assertEqual(sale.payment_method, "credit")
        self.assertEqual(sale.total, 150.15)

    def test_invalid_payment_method(self):
        """Testa que um método de pagamento inválido não deve ser aceito"""
        sale = Sale(customer="Maria", payment_method="bitcoin", total=300)
        with self.assertRaises(ValidationError) as context:
            sale.full_clean()
        self.assertIn("Valor 'bitcoin' não é uma opção válida", str(context.exception))

    def test_sale_str(self):
        """Testa a reprsentação em string do modelo."""
        sale = Sale.objects.create(total=99.99)
        self.assertEqual(str(sale), f"Sale #{sale.id} - 99.99")