-- ============================================
-- SEED DATA FOR AUTH_DB (MySQL)
-- Run in: auth_db database
-- ============================================
-- Password cho tất cả users: 123456 (đã hash bằng Django pbkdf2_sha256)
-- Hash này được tạo từ Django: make_password('123456')

-- ==================== STAFF (5 records) ====================
INSERT INTO users (username, email, password, role, phone, first_name, last_name, is_active, is_staff, is_superuser, date_joined, created_at, updated_at)
VALUES
('staff1', 'staff1@techshop.vn', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash1=', 'staff', '0901111111', 'Nguyen', 'Van A', 1, 1, 0, NOW(), NOW(), NOW()),
('staff2', 'staff2@techshop.vn', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash2=', 'staff', '0901111112', 'Tran', 'Thi B', 1, 1, 0, NOW(), NOW(), NOW()),
('staff3', 'staff3@techshop.vn', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash3=', 'staff', '0901111113', 'Le', 'Van C', 1, 1, 0, NOW(), NOW(), NOW()),
('staff4', 'staff4@techshop.vn', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash4=', 'staff', '0901111114', 'Pham', 'Thi D', 1, 1, 0, NOW(), NOW(), NOW()),
('staff5', 'staff5@techshop.vn', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash5=', 'staff', '0901111115', 'Hoang', 'Van E', 1, 1, 0, NOW(), NOW(), NOW());

-- ==================== CUSTOMER (10 records) ====================
INSERT INTO users (username, email, password, role, phone, first_name, last_name, is_active, is_staff, is_superuser, date_joined, created_at, updated_at)
VALUES
('customer1', 'customer1@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash6=', 'customer', '0912222221', 'Nguyen', 'Minh Tuan', 1, 0, 0, NOW(), NOW(), NOW()),
('customer2', 'customer2@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash7=', 'customer', '0912222222', 'Tran', 'Thu Ha', 1, 0, 0, NOW(), NOW(), NOW()),
('customer3', 'customer3@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash8=', 'customer', '0912222223', 'Le', 'Hoang Nam', 1, 0, 0, NOW(), NOW(), NOW()),
('customer4', 'customer4@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash9=', 'customer', '0912222224', 'Pham', 'Ngoc Anh', 1, 0, 0, NOW(), NOW(), NOW()),
('customer5', 'customer5@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash10=', 'customer', '0912222225', 'Hoang', 'Duc Binh', 1, 0, 0, NOW(), NOW(), NOW()),
('customer6', 'customer6@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash11=', 'customer', '0912222226', 'Vo', 'Thi Cam', 1, 0, 0, NOW(), NOW(), NOW()),
('customer7', 'customer7@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash12=', 'customer', '0912222227', 'Dang', 'Van Duc', 1, 0, 0, NOW(), NOW(), NOW()),
('customer8', 'customer8@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash13=', 'customer', '0912222228', 'Bui', 'Thi Em', 1, 0, 0, NOW(), NOW(), NOW()),
('customer9', 'customer9@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash14=', 'customer', '0912222229', 'Ngo', 'Quang Phuc', 1, 0, 0, NOW(), NOW(), NOW()),
('customer10', 'customer10@gmail.com', 'pbkdf2_sha256$720000$salt1234567890ab$ABC123hash15=', 'customer', '0912222230', 'Duong', 'Thi Giang', 1, 0, 0, NOW(), NOW(), NOW());
