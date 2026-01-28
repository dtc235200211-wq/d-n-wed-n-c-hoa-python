# Perfume Shop (Django)

## Chức năng
- Home hiển thị sản phẩm (seed data)
- Register / Login / Logout
- Dashboard
- CRUD Products
- Orders list + Create order (demo)
- Bootstrap responsive UI
- Template inheritance (base.html)

## Cài đặt & chạy (Windows)
```bat
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py seed
py manage.py runserver
```

## Link demo
- Home: http://127.0.0.1:8000/
- Products: http://127.0.0.1:8000/store/products/
- Orders: http://127.0.0.1:8000/orders/
- Admin: http://127.0.0.1:8000/admin/
