from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Product

def home(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "home.html", {"products": products})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "stock", "description", "category"]

def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "store/product_list.html", {"products": products})

@login_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "store/product_form.html", {"form": form, "title": "Create Product"})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "store/product_form.html", {"form": form, "title": "Edit Product"})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "store/product_delete.html", {"product": product})
