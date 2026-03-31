"""
Seed data script for Mobile Service
Run inside mobile-service container or with Django shell:
    docker exec -it mobile_service python manage.py shell < seed_mobiles.py
    OR
    python manage.py shell < seed_mobiles.py
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mobile_project.settings")
django.setup()

from mobile_app.models import Mobile
from decimal import Decimal

# Mobile data
mobiles = [
    {
        "name": "iPhone 15 Pro Max",
        "brand": "Apple",
        "price": Decimal("34990000"),
        "description": "iPhone cao cấp nhất với chip A17 Pro, camera 48MP và khung Titanium",
        "cpu": "Apple A17 Pro",
        "ram": "8GB",
        "storage": "256GB",
        "screen_size": "6.7 inch Super Retina XDR",
        "battery": "4422mAh",
        "stock": 20,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-15-pro-max-natural-titanium.png",
    },
    {
        "name": "iPhone 15",
        "brand": "Apple",
        "price": Decimal("22990000"),
        "description": "iPhone thế hệ mới với Dynamic Island, camera 48MP và cổng USB-C",
        "cpu": "Apple A16 Bionic",
        "ram": "6GB",
        "storage": "128GB",
        "screen_size": "6.1 inch Super Retina XDR",
        "battery": "3349mAh",
        "stock": 25,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-15-pink.png",
    },
    {
        "name": "Galaxy S24 Ultra",
        "brand": "Samsung",
        "price": Decimal("33990000"),
        "description": "Flagship Android với S Pen, camera 200MP và AI thông minh",
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "12GB",
        "storage": "256GB",
        "screen_size": "6.8 inch Dynamic AMOLED",
        "battery": "5000mAh",
        "stock": 18,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/s/a/samsung-galaxy-s24-ultra-titanium-gray.png",
    },
    {
        "name": "Galaxy S24",
        "brand": "Samsung",
        "price": Decimal("22990000"),
        "description": "Điện thoại Samsung cao cấp với AI Galaxy, màn hình sáng nhất",
        "cpu": "Exynos 2400",
        "ram": "8GB",
        "storage": "256GB",
        "screen_size": "6.2 inch Dynamic AMOLED",
        "battery": "4000mAh",
        "stock": 22,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/s/a/samsung-galaxy-s24-violet.png",
    },
    {
        "name": "Xiaomi 14 Ultra",
        "brand": "Xiaomi",
        "price": Decimal("27990000"),
        "description": "Camera Leica chuyên nghiệp, chip Snapdragon 8 Gen 3 mạnh mẽ",
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "16GB",
        "storage": "512GB",
        "screen_size": "6.73 inch LTPO AMOLED",
        "battery": "5000mAh",
        "stock": 12,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/x/i/xiaomi-14-ultra-black.png",
    },
    {
        "name": "OPPO Find X7 Ultra",
        "brand": "OPPO",
        "price": Decimal("25990000"),
        "description": "Camera kép periscope, hiệu năng flagship với sạc nhanh 100W",
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "16GB",
        "storage": "512GB",
        "screen_size": "6.82 inch LTPO AMOLED",
        "battery": "5000mAh",
        "stock": 10,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/o/p/oppo-find-x7-ultra.png",
    },
    {
        "name": "Google Pixel 8 Pro",
        "brand": "Google",
        "price": Decimal("26990000"),
        "description": "Camera AI thông minh nhất, cập nhật Android 7 năm",
        "cpu": "Google Tensor G3",
        "ram": "12GB",
        "storage": "256GB",
        "screen_size": "6.7 inch LTPO OLED",
        "battery": "5050mAh",
        "stock": 8,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/g/o/google-pixel-8-pro-bay.png",
    },
    {
        "name": "OnePlus 12",
        "brand": "OnePlus",
        "price": Decimal("21990000"),
        "description": "Flagship killer với Snapdragon 8 Gen 3, sạc nhanh 100W",
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "12GB",
        "storage": "256GB",
        "screen_size": "6.82 inch LTPO AMOLED",
        "battery": "5400mAh",
        "stock": 15,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/o/n/oneplus-12-silky-black.png",
    },
    {
        "name": "Realme GT 5 Pro",
        "brand": "Realme",
        "price": Decimal("16990000"),
        "description": "Hiệu năng flagship giá tốt, camera Sony IMX890 50MP",
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "12GB",
        "storage": "256GB",
        "screen_size": "6.78 inch LTPO AMOLED",
        "battery": "5400mAh",
        "stock": 20,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/r/e/realme-gt-5-pro.png",
    },
    {
        "name": "Vivo X100 Pro",
        "brand": "Vivo",
        "price": Decimal("24990000"),
        "description": "Camera ZEISS chuyên nghiệp, chip Dimensity 9300 mạnh mẽ",
        "cpu": "Dimensity 9300",
        "ram": "12GB",
        "storage": "256GB",
        "screen_size": "6.78 inch LTPO AMOLED",
        "battery": "5400mAh",
        "stock": 11,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/v/i/vivo-x100-pro.png",
    },
]

print("Creating mobiles...")
for data in mobiles:
    mobile, created = Mobile.objects.get_or_create(
        name=data["name"], brand=data["brand"], defaults=data
    )
    if created:
        print(f"  Created: {mobile.brand} {mobile.name}")
    else:
        print(f"  Exists: {mobile.brand} {mobile.name}")

print(f"\n✅ Done! Total mobiles: {Mobile.objects.count()}")
