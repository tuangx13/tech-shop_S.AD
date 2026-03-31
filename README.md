# Microservices E-commerce Platform

Dự án E-commerce sử dụng kiến trúc microservices với Django, React và Docker.

## Cấu trúc Project

```
kiemtra01/
├── .env                      # Environment variables
├── docker-compose.yml        # Docker orchestration
├── init-mysql.sql           # MySQL initialization
├── init-postgres.sql        # PostgreSQL initialization
├── auth-service/            # JWT Authentication (MySQL)
├── customer-service/        # Customer features (MySQL)
├── staff_service/           # Staff management (MySQL)
├── laptop_service/          # Laptop CRUD (PostgreSQL)
├── mobile-service/          # Mobile CRUD (PostgreSQL)
├── api-gateway/             # API Gateway with JWT middleware
└── frontend/                # React frontend (Customer & Staff UI)
```

## Các Service

### 1. Auth Service (Port 8000)
- JWT Authentication
- User registration/login
- Role-based access (customer/staff)
- Database: MySQL (auth_db)

### 2. Customer Service (Port 8001)
- Quản lý giỏ hàng
- Tìm kiếm sản phẩm
- Database: MySQL (customer_db)

### 3. Staff Service (Port 8002)
- Thêm/cập nhật sản phẩm
- Quản lý inventory
- Database: MySQL (staff_db)

### 4. Laptop Service (Port 8003)
- CRUD operations cho laptop
- Database: PostgreSQL (laptop_db)

### 5. Mobile Service (Port 8004)
- CRUD operations cho mobile
- Database: PostgreSQL (mobile_db)

### 6. API Gateway (Port 8080)
- Proxy requests đến các services
- JWT verification middleware
- Role-based routing

### 7. Frontend (Port 3000)
- React Single Page Application
- 2 giao diện riêng biệt:
  - Customer UI: Login, giỏ hàng, tìm kiếm (màu xanh dương)
  - Staff UI: Login, quản lý sản phẩm (màu xanh lá)

## Yêu cầu hệ thống

- Docker & Docker Compose
- Port available: 3000, 3306, 5432, 8000-8004, 8080

## Cài đặt và Chạy

### 1. Khởi động tất cả services
```bash
cd kiemtra01
docker-compose up --build
```

### 2. Chờ services khởi động (1-2 phút)

## Sử dụng Application

### Customer Interface
- Truy cập: http://localhost:3000/customer/login
- Đăng ký với role customer
- Tính năng: Xem sản phẩm, tìm kiếm, giỏ hàng
- Customer: customer1 - customer10
- Mật khẩu tất cả: 123456

### Staff Interface
- Truy cập: http://localhost:3000/staff/login
- Đăng ký với role staff
- Tính năng: Quản lý sản phẩm, thêm/sửa/xóa
- Staff: staff1 - staff5
- Mật khẩu tất cả: 123456

## Commands hữu ích

```bash
# Xem logs
docker-compose logs -f

# Stop services
docker-compose down

# Xóa tất cả (bao gồm data)
docker-compose down -v
```

## API Testing

### Đăng ký customer
```bash
curl -X POST http://localhost:8080/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"customer1","password":"123456","password_confirm":"123456","email":"c@test.com","role":"customer"}'
```

### Login
```bash
curl -X POST http://localhost:8080/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"customer1","password":"123456","role":"customer"}'
```

Xem thêm chi tiết trong file INSTRUCTIONS.md
