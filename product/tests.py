from django.test import TestCase
from django.db import IntegrityError
from .models import Category, Product
from datetime import date
from django.core.exceptions import ValidationError


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
