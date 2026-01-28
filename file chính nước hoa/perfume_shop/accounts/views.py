from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        msg = "Sai tài khoản hoặc mật khẩu!"
    return render(request, "accounts/login.html", {"msg": msg})

def register_view(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            msg = "Mật khẩu xác nhận không khớp!"
        elif User.objects.filter(username=username).exists():
            msg = "Username đã tồn tại!"
        else:
            User.objects.create_user(username=username, password=password)
            return redirect("login")

    return render(request, "accounts/register.html", {"msg": msg})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
