# Hướng dẫn Chạy và Test Project

## Bước 1: Khởi động Docker Compose

```bash
cd /c/kiemtra01
docker-compose up --build
```

Chờ khoảng 1-2 phút để tất cả services khởi động.

## Bước 2: Kiểm tra Services

### Kiểm tra health của các services:

```bash
# API Gateway
curl http://localhost:8080/health/

# Các services khác (trong Docker network)
docker-compose exec api-gateway curl http://auth-service:8000/api/auth/
```

## Bước 3: Test Authentication Flow

### 3.1. Đăng ký Customer

```bash
curl -X POST http://localhost:8080/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testcustomer",
    "email": "customer@test.com",
    "password": "password123",
    "password_confirm": "password123",
    "role": "customer"
  }'
```

### 3.2. Đăng ký Staff

```bash
curl -X POST http://localhost:8080/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "teststaff",
    "email": "staff@test.com",
    "password": "password123",
    "password_confirm": "password123",
    "role": "staff"
  }'
```

### 3.3. Login Customer

```bash
curl -X POST http://localhost:8080/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testcustomer",
    "password": "password123",
    "role": "customer"
  }'
```

Lưu token từ response để sử dụng cho các requests tiếp theo.

### 3.4. Login Staff

```bash
curl -X POST http://localhost:8080/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "teststaff",
    "password": "password123",
    "role": "staff"
  }'
```

## Bước 4: Test với Token

### Verify Token

```bash
curl -X GET http://localhost:8080/api/auth/verify/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### Get Current User Info

```bash
curl -X GET http://localhost:8080/api/auth/me/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Bước 5: Test Frontend

### Customer Interface

1. Mở browser: http://localhost:3000/customer/login
2. Đăng ký/đăng nhập với customer account
3. Test các tính năng:
   - Xem danh sách sản phẩm
   - Tìm kiếm sản phẩm
   - Thêm vào giỏ hàng
   - Xóa khỏi giỏ hàng

### Staff Interface

1. Mở browser: http://localhost:3000/staff/login
2. Đăng ký/đăng nhập với staff account
3. Test các tính năng:
   - Xem danh sách tất cả sản phẩm
   - Thêm sản phẩm mới
   - Cập nhật sản phẩm
   - Xóa sản phẩm

## Bước 6: Kiểm tra Databases

### MySQL (Auth, Customer, Staff)

```bash
# Access MySQL
docker-compose exec mysql mysql -u root -prootpassword

# Check databases
mysql> SHOW DATABASES;
mysql> USE auth_db;
mysql> SHOW TABLES;
mysql> SELECT * FROM users;
```

### PostgreSQL (Laptop, Mobile)

```bash
# Access PostgreSQL
docker-compose exec postgres psql -U postgres

# Check databases
\l
\c laptop_db
\dt
```

## Bước 7: Test Role-Based Access

### Customer cố gắng truy cập Staff endpoint (sẽ bị từ chối)

```bash
curl -X GET http://localhost:8080/api/staff/products/ \
  -H "Authorization: Bearer CUSTOMER_TOKEN"

# Expected: 403 Forbidden
```

### Staff cố gắng truy cập Customer endpoint (sẽ bị từ chối)

```bash
curl -X GET http://localhost:8080/api/customer/cart/ \
  -H "Authorization: Bearer STAFF_TOKEN"

# Expected: 403 Forbidden
```

## Common Issues and Solutions

### Issue 1: Port already in use
```bash
# Find process using port
lsof -i :3000
lsof -i :8080

# Kill process or change port in docker-compose.yml
```

### Issue 2: Services not starting
```bash
# Check logs
docker-compose logs auth-service
docker-compose logs mysql

# Restart specific service
docker-compose restart auth-service
```

### Issue 3: Database connection error
```bash
# Wait for healthcheck
docker-compose ps

# Manually run migrations
docker-compose exec auth-service python manage.py migrate
```

### Issue 4: Frontend can't connect to API
```bash
# Check API Gateway logs
docker-compose logs api-gateway

# Verify network
docker network ls
docker network inspect kiemtra01_microservices_net
```

## Cleanup

### Stop all services
```bash
docker-compose down
```

### Remove all data (including databases)
```bash
docker-compose down -v
```

### Remove all images
```bash
docker-compose down --rmi all
```

## Development Tips

### Watch logs in real-time
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f auth-service
```

### Execute commands in running container
```bash
# Django shell
docker-compose exec auth-service python manage.py shell

# Create superuser
docker-compose exec auth-service python manage.py createsuperuser

# Run tests
docker-compose exec auth-service python manage.py test
```

### Rebuild single service
```bash
docker-compose up -d --no-deps --build auth-service
```

## Architecture Verification

Verify the microservices architecture:

1. ✅ Each service runs independently
2. ✅ Services communicate through API Gateway
3. ✅ JWT authentication works across services
4. ✅ Role-based access control is enforced
5. ✅ MySQL services are isolated
6. ✅ PostgreSQL services are isolated
7. ✅ Frontend has separate UIs for customer/staff
8. ✅ API Gateway properly routes and validates requests

## Next Steps

1. Add sample data to product services
2. Implement full CRUD operations in frontend
3. Add pagination and filtering
4. Implement proper error handling
5. Add unit and integration tests
6. Setup CI/CD pipeline
7. Add API documentation (Swagger/OpenAPI)
8. Implement caching layer
9. Add monitoring and logging
10. Security hardening

