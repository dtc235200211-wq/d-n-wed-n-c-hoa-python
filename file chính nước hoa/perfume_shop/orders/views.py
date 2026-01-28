from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all().order_by("-created_at")
    else:
        orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_list.html", {"orders": orders})

@login_required
def order_create(request):
    Order.objects.create(user=request.user, status="pending")
    return redirect("order_list")
