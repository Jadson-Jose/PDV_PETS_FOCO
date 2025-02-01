from django.db import models


class Supplier(models.Model):
    name = models.CharField( max_length=50, verbose_name="Nome")
    email = models.EmailField( verbose_name="E-mail", blank=True, null=True)
    phone = models.CharField( max_length=20, verbose_name="Telefone", blank=True, null=True)
    address = models.TextField(verbose_name="Endereço", blank=True, null=True)
    company_name = models.CharField( max_length=255, verbose_name="Nome da empresa", blank=True, null=True)
    tax_id = models.CharField( max_length=20, verbose_name="CNPJ/CPF", unique=True, blank=True, null=True)
    created_at = models.DateTimeField( auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
