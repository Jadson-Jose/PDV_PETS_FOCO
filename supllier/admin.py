from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company_name", "tax_id", "created_at")
    search_fields = ("name", "company_name", "tax_id")
    list_filter = ("created_at")
