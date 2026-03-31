-- ============================================
-- SEED DATA FOR LAPTOP_DB (PostgreSQL)
-- Run in: laptop_db database
-- ============================================

INSERT INTO laptop_app_laptop (name, brand, price, description, cpu, ram, storage, screen_size, stock, image_url, created_at, updated_at)
VALUES
('MacBook Pro 14', 'Apple', 52990000, 'MacBook Pro 14 inch với chip M3 Pro, hiệu năng mạnh mẽ cho công việc chuyên nghiệp', 'Apple M3 Pro', '18GB', '512GB SSD', '14.2 inch', 15, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/m/a/macbook-pro-14-inch-m3-pro-2023.png', NOW(), NOW()),

('MacBook Air M2', 'Apple', 27990000, 'MacBook Air siêu mỏng nhẹ với chip M2, thời lượng pin cả ngày', 'Apple M2', '8GB', '256GB SSD', '13.6 inch', 25, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/m/a/macbook-air-m2-2022-midnight.png', NOW(), NOW()),

('ThinkPad X1 Carbon Gen 11', 'Lenovo', 45990000, 'Laptop doanh nhân cao cấp, siêu nhẹ chỉ 1.12kg với màn hình OLED', 'Intel Core i7-1365U', '16GB', '512GB SSD', '14 inch OLED', 10, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/l/e/lenovo-thinkpad-x1-carbon-gen-11.png', NOW(), NOW()),

('Dell XPS 15', 'Dell', 42990000, 'Laptop cao cấp với màn hình OLED 3.5K tuyệt đẹp, thiết kế sang trọng', 'Intel Core i7-13700H', '16GB', '512GB SSD', '15.6 inch OLED', 12, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/d/e/dell-xps-15-9530.png', NOW(), NOW()),

('ASUS ROG Strix G16', 'ASUS', 35990000, 'Laptop gaming mạnh mẽ với RTX 4060, màn hình 165Hz mượt mà', 'Intel Core i7-13650HX', '16GB', '512GB SSD', '16 inch 165Hz', 20, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/a/s/asus-rog-strix-g16-2023.png', NOW(), NOW()),

('HP Pavilion 15', 'HP', 18990000, 'Laptop văn phòng với hiệu năng ổn định, thiết kế hiện đại', 'Intel Core i5-1335U', '8GB', '512GB SSD', '15.6 inch FHD', 30, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/h/p/hp-pavilion-15-eg3098tu.png', NOW(), NOW()),

('Acer Nitro 5', 'Acer', 23990000, 'Laptop gaming giá rẻ với RTX 3050, phù hợp cho game thủ mới', 'Intel Core i5-12500H', '8GB', '512GB SSD', '15.6 inch 144Hz', 18, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/a/c/acer-nitro-5-an515-58.png', NOW(), NOW()),

('MSI Katana 15', 'MSI', 28990000, 'Laptop gaming với RTX 4050, thiết kế mạnh mẽ và đèn RGB', 'Intel Core i7-13620H', '16GB', '512GB SSD', '15.6 inch 144Hz', 14, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/m/s/msi-katana-15-b13vek.png', NOW(), NOW()),

('Surface Laptop 5', 'Microsoft', 32990000, 'Laptop cao cấp từ Microsoft với màn hình cảm ứng PixelSense', 'Intel Core i7-1265U', '16GB', '512GB SSD', '13.5 inch', 8, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/s/u/surface-laptop-5.png', NOW(), NOW()),

('LG Gram 17', 'LG', 38990000, 'Laptop 17 inch siêu nhẹ chỉ 1.35kg, pin 19.5 tiếng sử dụng', 'Intel Core i7-1360P', '16GB', '512GB SSD', '17 inch WQXGA', 6, 'https://cdn2.cellphones.com.vn/x/media/catalog/product/l/g/lg-gram-17-2023.png', NOW(), NOW());
