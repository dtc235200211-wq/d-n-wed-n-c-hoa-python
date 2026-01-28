from django.contrib import admin
from django.urls import path, include
from store.views import home
from accounts.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("store/", include("store.urls")),
    path("orders/", include("orders.urls")),

    path("dashboard/", dashboard, name="dashboard"),
]
