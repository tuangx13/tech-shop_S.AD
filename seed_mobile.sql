-- ============================================
-- SEED DATA FOR MOBILE_DB (PostgreSQL)
-- Run in: mobile_db database
-- ============================================

INSERT INTO mobile_app_mobile (name, brand, price, description, cpu, ram, storage, screen_size, battery, stock, image_url, created_at, updated_at)
VALUES
('iPhone 15 Pro Max', 'Apple', 34990000, 'iPhone cao cấp nhất với chip A17 Pro, camera 48MP và khung Titanium', 'Apple A17 Pro', '8GB', '256GB', '6.7 inch Super Retina XDR', '4422mAh', 20, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-15-pro-max-natural-titanium.png', NOW(), NOW()),

('iPhone 15', 'Apple', 22990000, 'iPhone thế hệ mới với Dynamic Island, camera 48MP và cổng USB-C', 'Apple A16 Bionic', '6GB', '128GB', '6.1 inch Super Retina XDR', '3349mAh', 25, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-15-pink.png', NOW(), NOW()),

('Samsung Galaxy S24 Ultra', 'Samsung', 33990000, 'Flagship Android với S Pen, camera 200MP và AI thông minh', 'Snapdragon 8 Gen 3', '12GB', '256GB', '6.8 inch Dynamic AMOLED', '5000mAh', 18, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/s/a/samsung-galaxy-s24-ultra-titanium-gray.png', NOW(), NOW()),

('Samsung Galaxy S24', 'Samsung', 22990000, 'Điện thoại Samsung cao cấp với AI Galaxy, màn hình sáng nhất', 'Exynos 2400', '8GB', '256GB', '6.2 inch Dynamic AMOLED', '4000mAh', 22, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/s/a/samsung-galaxy-s24-violet.png', NOW(), NOW()),

('Xiaomi 14 Ultra', 'Xiaomi', 27990000, 'Camera Leica chuyên nghiệp, chip Snapdragon 8 Gen 3 mạnh mẽ', 'Snapdragon 8 Gen 3', '16GB', '512GB', '6.73 inch LTPO AMOLED', '5000mAh', 12, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/x/i/xiaomi-14-ultra-black.png', NOW(), NOW()),

('OPPO Find X7 Ultra', 'OPPO', 25990000, 'Camera kép periscope, hiệu năng flagship với sạc nhanh 100W', 'Snapdragon 8 Gen 3', '16GB', '512GB', '6.82 inch LTPO AMOLED', '5000mAh', 10, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/o/p/oppo-find-x7-ultra.png', NOW(), NOW()),

('Google Pixel 8 Pro', 'Google', 26990000, 'Camera AI thông minh nhất, cập nhật Android 7 năm', 'Google Tensor G3', '12GB', '256GB', '6.7 inch LTPO OLED', '5050mAh', 8, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/g/o/google-pixel-8-pro-bay.png', NOW(), NOW()),

('OnePlus 12', 'OnePlus', 21990000, 'Flagship killer với Snapdragon 8 Gen 3, sạc nhanh 100W', 'Snapdragon 8 Gen 3', '12GB', '256GB', '6.82 inch LTPO AMOLED', '5400mAh', 15, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/o/n/oneplus-12-silky-black.png', NOW(), NOW()),

('Realme GT 5 Pro', 'Realme', 16990000, 'Hiệu năng flagship giá tốt, camera Sony IMX890 50MP', 'Snapdragon 8 Gen 3', '12GB', '256GB', '6.78 inch LTPO AMOLED', '5400mAh', 20, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/r/e/realme-gt-5-pro.png', NOW(), NOW()),

('Vivo X100 Pro', 'Vivo', 24990000, 'Camera ZEISS chuyên nghiệp, chip Dimensity 9300 mạnh mẽ', 'Dimensity 9300', '12GB', '256GB', '6.78 inch LTPO AMOLED', '5400mAh', 11, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/v/i/vivo-x100-pro.png', NOW(), NOW());
