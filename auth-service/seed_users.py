"""
Seed data script for Auth Service
Run inside auth-service container or with Django shell:
    docker exec -it auth_service python manage.py shell < seed_users.py
    OR
    python manage.py shell < seed_users.py
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_project.settings")
django.setup()

from authentication.models import User

# Clear existing test data (optional)
# User.objects.filter(username__startswith='staff').delete()
# User.objects.filter(username__startswith='customer').delete()

# ==================== STAFF (5 records) ====================
staff_data = [
    {
        "username": "staff1",
        "email": "staff1@techshop.vn",
        "first_name": "Nguyen",
        "last_name": "Van A",
        "phone": "0901111111",
    },
    {
        "username": "staff2",
        "email": "staff2@techshop.vn",
        "first_name": "Tran",
        "last_name": "Thi B",
        "phone": "0901111112",
    },
    {
        "username": "staff3",
        "email": "staff3@techshop.vn",
        "first_name": "Le",
        "last_name": "Van C",
        "phone": "0901111113",
    },
    {
        "username": "staff4",
        "email": "staff4@techshop.vn",
        "first_name": "Pham",
        "last_name": "Thi D",
        "phone": "0901111114",
    },
    {
        "username": "staff5",
        "email": "staff5@techshop.vn",
        "first_name": "Hoang",
        "last_name": "Van E",
        "phone": "0901111115",
    },
]

print("Creating staff users...")
for data in staff_data:
    if not User.objects.filter(username=data["username"]).exists():
        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password="123456",
            role="staff",
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data["phone"],
        )
        print(f"  Created: {user.username}")
    else:
        print(f"  Exists: {data['username']}")

# ==================== CUSTOMER (10 records) ====================
customer_data = [
    {
        "username": "customer1",
        "email": "customer1@gmail.com",
        "first_name": "Nguyen",
        "last_name": "Minh Tuan",
        "phone": "0912222221",
    },
    {
        "username": "customer2",
        "email": "customer2@gmail.com",
        "first_name": "Tran",
        "last_name": "Thu Ha",
        "phone": "0912222222",
    },
    {
        "username": "customer3",
        "email": "customer3@gmail.com",
        "first_name": "Le",
        "last_name": "Hoang Nam",
        "phone": "0912222223",
    },
    {
        "username": "customer4",
        "email": "customer4@gmail.com",
        "first_name": "Pham",
        "last_name": "Ngoc Anh",
        "phone": "0912222224",
    },
    {
        "username": "customer5",
        "email": "customer5@gmail.com",
        "first_name": "Hoang",
        "last_name": "Duc Binh",
        "phone": "0912222225",
    },
    {
        "username": "customer6",
        "email": "customer6@gmail.com",
        "first_name": "Vo",
        "last_name": "Thi Cam",
        "phone": "0912222226",
    },
    {
        "username": "customer7",
        "email": "customer7@gmail.com",
        "first_name": "Dang",
        "last_name": "Van Duc",
        "phone": "0912222227",
    },
    {
        "username": "customer8",
        "email": "customer8@gmail.com",
        "first_name": "Bui",
        "last_name": "Thi Em",
        "phone": "0912222228",
    },
    {
        "username": "customer9",
        "email": "customer9@gmail.com",
        "first_name": "Ngo",
        "last_name": "Quang Phuc",
        "phone": "0912222229",
    },
    {
        "username": "customer10",
        "email": "customer10@gmail.com",
        "first_name": "Duong",
        "last_name": "Thi Giang",
        "phone": "0912222230",
    },
]

print("\nCreating customer users...")
for data in customer_data:
    if not User.objects.filter(username=data["username"]).exists():
        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password="123456",
            role="customer",
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data["phone"],
        )
        print(f"  Created: {user.username}")
    else:
        print(f"  Exists: {data['username']}")

print("\n✅ Done! Created 5 staff + 10 customer accounts")
print("   Password for all: 123456")
