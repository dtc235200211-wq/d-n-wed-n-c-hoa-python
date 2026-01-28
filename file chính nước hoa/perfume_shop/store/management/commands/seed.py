from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = "Seed sample data"

    def handle(self, *args, **kwargs):
        cat1, _ = Category.objects.get_or_create(name="Nước hoa nam")
        cat2, _ = Category.objects.get_or_create(name="Nước hoa nữ")

        Product.objects.get_or_create(
            name="Dior Sauvage",
            brand="Dior",
            price=2500000,
            stock=10,
            category=cat1,
        )
        Product.objects.get_or_create(
            name="Chanel Coco Mademoiselle",
            brand="Chanel",
            price=3200000,
            stock=8,
            category=cat2,
        )

        self.stdout.write(self.style.SUCCESS("Seed data success!"))
