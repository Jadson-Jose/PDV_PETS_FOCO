from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Supplier
from .forms import SupplierForm


def suplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, "Suppliers/supplier_list.html", {'suppliers': suppliers})

def supplier_create(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("supplier_list")
    else:
        form = SupplierForm()
    return render(request, "suppliers/supplier_form.html")

def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk) 
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if  form.is_valid():
            form.save()
            return redirect("supplier_list")
    else:
        form = SupplierForm(instance=supplier)
    return render(request, "supplietr/supplier_form.html", {"form":form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        supplier.delete()
        return redirect("supplier_list")
    return render(request, "supplier/supplier_confirm_delete.html", {"supplier":supplier})
