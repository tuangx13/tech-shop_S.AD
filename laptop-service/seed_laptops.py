"""
Seed data script for Laptop Service
Run inside laptop-service container or with Django shell:
    docker exec -it laptop_service python manage.py shell < seed_laptops.py
    OR
    python manage.py shell < seed_laptops.py
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laptop_project.settings")
django.setup()

from laptop_app.models import Laptop
from decimal import Decimal

# Laptop data
laptops = [
    {
        "name": "MacBook Pro 14",
        "brand": "Apple",
        "price": Decimal("52990000"),
        "description": "MacBook Pro 14 inch với chip M3 Pro, hiệu năng mạnh mẽ cho công việc chuyên nghiệp",
        "cpu": "Apple M3 Pro",
        "ram": "18GB",
        "storage": "512GB SSD",
        "screen_size": "14.2 inch",
        "stock": 15,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/m/a/macbook-pro-14-inch-m3-pro-2023.png",
    },
    {
        "name": "MacBook Air M2",
        "brand": "Apple",
        "price": Decimal("27990000"),
        "description": "MacBook Air siêu mỏng nhẹ với chip M2, thời lượng pin cả ngày",
        "cpu": "Apple M2",
        "ram": "8GB",
        "storage": "256GB SSD",
        "screen_size": "13.6 inch",
        "stock": 25,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/m/a/macbook-air-m2-2022-midnight.png",
    },
    {
        "name": "ThinkPad X1 Carbon Gen 11",
        "brand": "Lenovo",
        "price": Decimal("45990000"),
        "description": "Laptop doanh nhân cao cấp, siêu nhẹ chỉ 1.12kg với màn hình OLED",
        "cpu": "Intel Core i7-1365U",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "14 inch OLED",
        "stock": 10,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/l/e/lenovo-thinkpad-x1-carbon-gen-11.png",
    },
    {
        "name": "Dell XPS 15",
        "brand": "Dell",
        "price": Decimal("42990000"),
        "description": "Laptop cao cấp với màn hình OLED 3.5K tuyệt đẹp, thiết kế sang trọng",
        "cpu": "Intel Core i7-13700H",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "15.6 inch OLED",
        "stock": 12,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/d/e/dell-xps-15-9530.png",
    },
    {
        "name": "ASUS ROG Strix G16",
        "brand": "ASUS",
        "price": Decimal("35990000"),
        "description": "Laptop gaming mạnh mẽ với RTX 4060, màn hình 165Hz mượt mà",
        "cpu": "Intel Core i7-13650HX",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "16 inch 165Hz",
        "stock": 20,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/a/s/asus-rog-strix-g16-2023.png",
    },
    {
        "name": "HP Pavilion 15",
        "brand": "HP",
        "price": Decimal("18990000"),
        "description": "Laptop văn phòng với hiệu năng ổn định, thiết kế hiện đại",
        "cpu": "Intel Core i5-1335U",
        "ram": "8GB",
        "storage": "512GB SSD",
        "screen_size": "15.6 inch FHD",
        "stock": 30,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/h/p/hp-pavilion-15-eg3098tu.png",
    },
    {
        "name": "Acer Nitro 5",
        "brand": "Acer",
        "price": Decimal("23990000"),
        "description": "Laptop gaming giá rẻ với RTX 3050, phù hợp cho game thủ mới",
        "cpu": "Intel Core i5-12500H",
        "ram": "8GB",
        "storage": "512GB SSD",
        "screen_size": "15.6 inch 144Hz",
        "stock": 18,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/a/c/acer-nitro-5-an515-58.png",
    },
    {
        "name": "MSI Katana 15",
        "brand": "MSI",
        "price": Decimal("28990000"),
        "description": "Laptop gaming với RTX 4050, thiết kế mạnh mẽ và đèn RGB",
        "cpu": "Intel Core i7-13620H",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "15.6 inch 144Hz",
        "stock": 14,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/m/s/msi-katana-15-b13vek.png",
    },
    {
        "name": "Surface Laptop 5",
        "brand": "Microsoft",
        "price": Decimal("32990000"),
        "description": "Laptop cao cấp từ Microsoft với màn hình cảm ứng PixelSense",
        "cpu": "Intel Core i7-1265U",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "13.5 inch",
        "stock": 8,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/s/u/surface-laptop-5.png",
    },
    {
        "name": "LG Gram 17",
        "brand": "LG",
        "price": Decimal("38990000"),
        "description": "Laptop 17 inch siêu nhẹ chỉ 1.35kg, pin 19.5 tiếng sử dụng",
        "cpu": "Intel Core i7-1360P",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen_size": "17 inch WQXGA",
        "stock": 6,
        "image_url": "https://cdn2.cellphones.com.vn/x/media/catalog/product/l/g/lg-gram-17-2023.png",
    },
]

print("Creating laptops...")
for data in laptops:
    laptop, created = Laptop.objects.get_or_create(
        name=data["name"], brand=data["brand"], defaults=data
    )
    if created:
        print(f"  Created: {laptop.brand} {laptop.name}")
    else:
        print(f"  Exists: {laptop.brand} {laptop.name}")

print(f"\n✅ Done! Total laptops: {Laptop.objects.count()}")
