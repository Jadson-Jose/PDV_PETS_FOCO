from django.test import TestCase
from .models import Sale
from django.core.exceptions import ValidationError

class SaleModelTest(TestCase):
    
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
        """Testa a representação em string do modelo."""
        sale = Sale.objects.create(total=99.99)
        sale.refresh_from_db()
        self.assertEqual(str(sale), f"Sale #{sale.id} - 99.99")

    def test_create_sale(self):
        """Testa a criação de uma venda."""
        sale = Sale.objects.create(total=150.75)
        self.assertEqual(sale.total, 150.75)
        self.assertIsNotNone(sale.id)

    def test_sale_invalid_total(self):
        """Testa a atualização do total da venda"""
        sale = Sale.objects.create(total=99.99)
        sale.total=120.00
        sale.save()
        self.assertEqual(sale.total, 120.00)

    def test_sale_negative_total(self):
        sale = Sale(customer="Cliente", total=-10.00)
        with self.assertRaises(ValidationError):
            sale.full_clean()

    def test_delete_sale(self):
        sale = Sale.objects.create(total=50.00)
        sale_id = sale.id
        sale.delete()
        self.assertFalse(Sale.objects.filter(id=sale_id).exists())

    def test_sale_extreme_total_values(self):
        sale1 = Sale.objects.create(total=99999999.99)
        sale2 = Sale.objects.create(total=0.01)
        self.assertEqual(sale1.total,99999999.99)
        self.assertEqual(sale2.total, 0.01)