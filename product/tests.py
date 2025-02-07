from django.test import TestCase
from django.db import IntegrityError
from .models import Category, Product
from datetime import date
from django.core.exceptions import ValidationError
import time


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = Category.objects.create(
            name="Ração",
            description="Ração para cães e gatos"
        )
        self.assertEqual(category.name, "Ração")
        self.assertEqual(category.description, "Ração para cães e gatos")

    def test_category_name_max_length(self):
        category = Category(name="a" * 101)
        with self.assertRaises(ValidationError) as context:
            category.full_clean()
        self.assertIn(
            "Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 101).",
            context.exception.messages)

    def test_category_name_unique(self):
        Category.objects.create(name="Ração")
        with self.assertRaises(IntegrityError):
            Category.objects.create(name="Ração")

    def test_category_description_blank_and_null(self):
        category = Category.objects.create(name="Brinquedo")
        self.assertEqual(category.description, "")

        category2 = Category.objects.create(name="Acessório", description=None)
        self.assertIsNone(category2.description)

    def test_category_str_representation(self):
        category = Category.objects.create(name="Higiene")
        self.assertEqual(str(category), "Higiene")


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Ração")

    def test_product_creation(self):

        expiration_date = date(2024, 12, 31)

        product = Product.objects.create(
            name="Ração para cães",
            description="Ração para cães adultos",
            price=50.00,
            stock=100,
            category=self.category,
            barcode="1234567890",
            expiration_date=expiration_date
        )
        self.assertEqual(product.name, "Ração para cães")
        self.assertEqual(product.description, "Ração para cães adultos")
        self.assertEqual(product.price, 50.00)
        self.assertEqual(product.stock, 100)
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.barcode, "1234567890")
        self.assertEqual(product.expiration_date, expiration_date)
        self.assertIsNotNone(product.created_at)
        self.assertIsNotNone(product.updated_at)

    def test_product_creation_without_expiration_date(self):
        product = Product.objects.create(
            name="Teste de Produto",
            description="Teste de descrição",
            price=29.99,
            stock=50,
            category=self.category,
            barcode="0987654321"
        )
        self.assertIsNone(product.expiration_date)

    def test_product_barcode_uniqueness(self):
        Product.objects.create(
            name="Teste de Produto 2",
            description="Teste de descrição 2",
            price=39.99,
            stock=25,
            category=self.category,
            barcode="1122334455"
        )
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Teste de Prduto 3",
                description="Teste de descrição 2",
                price=49.99,
                stock=75,
                category=self.category,
                barcode="1122334455"
            )

    def test_product_price_positive(self):
        product = Product(
            name="Teste de Produto 4",
            description="Teste de descrição 4",
            price=-10.00,
            stock=75,
            category=self.category,
            barcode=5544332211
        )
        with self.assertRaises(ValidationError):
            product.full_clean()
            product.save()

    def test_product_stock_positive(self):
        product = Product(
            name="Teste de Produto 5",
            description="Teste de descrição 5",
            price=10.00,
            stock=-5,
            category=self.category,
            barcode="66767889900"
        )
        with self.assertRaises(ValidationError):
            product.full_clean()
            product.save()

    def test_product_category_relationship(self):
        product = Product(
            name="Teste de Produto 6",
            description="Teste de descrição 6",
            price=15.00,
            stock=60,
            category=self.category,
            barcode="12121121211212"
        )
        product.save()
        self.assertEqual(product.category, self.category)
        self.assertEqual(self.category.products.count(), 1)

    def test_product_srt_representation(self):
        product = Product(
            name="Teste de Produto 7",
            description="Teste de descrição 7",
            price=20.00,
            stock=80,
            category=self.category,
            barcode="131313131313"
        )
        product.save()
        self.assertEqual(str(product), product.name)

    def test_product_updated_at_field(self):
        product = Product.objects.create(
            name="Teste Updated At",
            description="Teste de updated_at",
            price=10.00,
            stock=10,
            category=self.category,
            barcode="TEST1234"
        )
        old_updated_at = product.updated_at
        # Aguarda um segundo para garantir a diferença de tempo
        time.sleep(1)
        product.description = "Descrição atualizada"
        product.save()
        product.refresh_from_db()
        self.assertGreater(product.updated_at, old_updated_at)

    def test_product_name_max_legth(self):
        product = Product.objects.create(
            name="a" * 201,
            description="Teste de Descricao",
            price=45.23,
            stock=98,
            category=self.category,
            barcode="TSTE02032"
        )
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_barcode_max_length(self):
        product = Product(
            name="Produto com barcode longo",
            description="Teste de descrição",
            price=10.00,
            stock=10,
            category=self.category,
            barcode="a" * 200
        )
        with self.assertRaises(ValidationError):
            product.full_clean()
