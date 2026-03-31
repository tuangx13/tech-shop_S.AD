#!/bin/bash
# ============================================
# SEED ALL DATA SCRIPT
# Run this after docker-compose up
# ============================================

echo "🌱 Seeding data for all services..."
echo ""

# Seed Users (Staff + Customer)
echo "📦 Seeding Auth Service (Users)..."
docker exec -i auth_service python manage.py shell < auth-service/seed_users.py
echo ""

# Seed Laptops
echo "💻 Seeding Laptop Service..."
docker exec -i laptop_service python manage.py shell < laptop-service/seed_laptops.py
echo ""

# Seed Mobiles
echo "📱 Seeding Mobile Service..."
docker exec -i mobile_service python manage.py shell < mobile-service/seed_mobiles.py
echo ""

echo "============================================"
echo "✅ All data seeded successfully!"
echo ""
echo "📋 Summary:"
echo "   - Staff accounts: 5 (staff1 - staff5)"
echo "   - Customer accounts: 10 (customer1 - customer10)"
echo "   - Laptops: 10 products"
echo "   - Mobiles: 10 products"
echo ""
echo "🔑 Login credentials:"
echo "   - All accounts password: 123456"
echo "============================================"
