from django.test import TestCase
from django.db import IntegrityError
from .models import Category
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

# TODO CONTINUAR OS TESTES PRODUCT and more
