import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .forms import CustomerRegistrationForm
from .models import Cart, CartItem


# ==================== TEMPLATE VIEWS ====================
def customer_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
    return render(request, "customer_app/login.html")


def customer_register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user_id=user.id)
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomerRegistrationForm()
    return render(request, "customer_app/register.html", {"form": form})


def customer_logout(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
    laptops = []
    mobiles = []
    try:
        resp = requests.get(f"{settings.LAPTOP_SERVICE_URL}/api/laptops/", timeout=5)
        if resp.status_code == 200:
            laptops = resp.json()
    except Exception:
        pass
    try:
        resp = requests.get(f"{settings.MOBILE_SERVICE_URL}/api/mobiles/", timeout=5)
        if resp.status_code == 200:
            mobiles = resp.json()
    except Exception:
        pass

    context = {
        "laptops": laptops[:6],
        "mobiles": mobiles[:6],
        "cart": cart,
    }
    return render(request, "customer_app/dashboard.html", context)


@login_required
def search_products(request):
    query = request.GET.get("q", "")
    laptops = []
    mobiles = []
    if query:
        try:
            resp = requests.get(
                f"{settings.LAPTOP_SERVICE_URL}/api/laptops/search/",
                params={"q": query},
                timeout=5,
            )
            if resp.status_code == 200:
                laptops = resp.json()
        except Exception:
            pass
        try:
            resp = requests.get(
                f"{settings.MOBILE_SERVICE_URL}/api/mobiles/search/",
                params={"q": query},
                timeout=5,
            )
            if resp.status_code == 200:
                mobiles = resp.json()
        except Exception:
            pass

    context = {
        "query": query,
        "laptops": laptops,
        "mobiles": mobiles,
    }
    return render(request, "customer_app/search.html", context)


@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_type = request.POST.get("product_type")
        product_name = request.POST.get("product_name")
        product_price = request.POST.get("product_price")

        cart, _ = Cart.objects.get_or_create(user_id=request.user.id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            product_type=product_type,
            defaults={
                "product_name": product_name,
                "product_price": product_price,
                "quantity": 1,
            },
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        messages.success(request, f'Đã thêm "{product_name}" vào giỏ hàng!')
    return redirect(request.META.get("HTTP_REFERER", "dashboard"))


@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user_id=request.user.id)
    return render(request, "customer_app/cart.html", {"cart": cart})


@login_required
def remove_from_cart(request, item_id):
    try:
        cart = Cart.objects.get(user_id=request.user.id)
        item = CartItem.objects.get(id=item_id, cart=cart)
        item.delete()
        messages.success(request, "Đã xóa sản phẩm khỏi giỏ hàng.")
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        messages.error(request, "Không tìm thấy sản phẩm.")
    return redirect("cart")


# ==================== REST API VIEWS ====================
@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_cart(request):
    """API endpoint for cart operations"""
    # Get user_id from request header (passed by gateway)
    user_id = request.headers.get("X-User-Id")

    if not user_id:
        return JsonResponse({"error": "User authentication required"}, status=401)

    try:
        user_id = int(user_id)
    except ValueError:
        return JsonResponse({"error": "Invalid user ID"}, status=400)

    # Get or create cart for this user
    cart, _ = Cart.objects.get_or_create(user_id=user_id)

    if request.method == "GET":
        # Return cart with items
        items = []
        for item in cart.items.all():
            items.append(
                {
                    "id": item.id,
                    "product_id": item.product_id,
                    "product_type": item.product_type,
                    "product_name": item.product_name,
                    "product_price": str(item.product_price),
                    "quantity": item.quantity,
                    "total_price": str(item.total_price),
                }
            )
        return JsonResponse(
            {
                "id": cart.id,
                "items": items,
                "total_items": cart.total_items,
                "total_price": str(cart.total_price),
            }
        )

    elif request.method == "POST":
        # Add item to cart
        try:
            data = json.loads(request.body)
            product_id = data.get("product_id")
            product_type = data.get("product_type")
            product_name = data.get("product_name")
            product_price = data.get("product_price")
            quantity = data.get("quantity", 1)

            if not all([product_id, product_type, product_name, product_price]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product_id=product_id,
                product_type=product_type,
                defaults={
                    "product_name": product_name,
                    "product_price": product_price,
                    "quantity": quantity,
                },
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return JsonResponse(
                {
                    "message": f"Added {product_name} to cart",
                    "item": {
                        "id": cart_item.id,
                        "product_id": cart_item.product_id,
                        "product_type": cart_item.product_type,
                        "product_name": cart_item.product_name,
                        "quantity": cart_item.quantity,
                    },
                },
                status=201 if created else 200,
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
def api_cart_item(request, item_id):
    """API endpoint for single cart item operations"""
    user_id = request.headers.get("X-User-Id")

    if not user_id:
        return JsonResponse({"error": "User authentication required"}, status=401)

    try:
        cart = Cart.objects.get(user_id=user_id)
        item = CartItem.objects.get(id=item_id, cart=cart)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return JsonResponse({"error": "Item not found"}, status=404)

    if request.method == "PUT":
        # Update quantity
        try:
            data = json.loads(request.body)
            quantity = data.get("quantity", 1)
            if quantity <= 0:
                item.delete()
                return JsonResponse({"message": "Item removed from cart"})
            item.quantity = quantity
            item.save()
            return JsonResponse(
                {
                    "message": "Cart updated",
                    "item": {
                        "id": item.id,
                        "quantity": item.quantity,
                        "total_price": str(item.total_price),
                    },
                }
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    elif request.method == "DELETE":
        item.delete()
        return JsonResponse({"message": "Item removed from cart"})


@csrf_exempt
@require_http_methods(["GET"])
def api_search(request):
    """API endpoint for product search"""
    query = request.GET.get("q", "")
    results = {"laptops": [], "mobiles": []}

    if query:
        # Search laptops
        try:
            resp = requests.get(
                f"{settings.LAPTOP_SERVICE_URL}/api/laptops/", timeout=5
            )
            if resp.status_code == 200:
                laptops = resp.json()
                # Filter by query
                results["laptops"] = [
                    l
                    for l in laptops
                    if query.lower() in l.get("name", "").lower()
                    or query.lower() in l.get("brand", "").lower()
                    or query.lower() in l.get("description", "").lower()
                ]
        except Exception:
            pass

        # Search mobiles
        try:
            resp = requests.get(
                f"{settings.MOBILE_SERVICE_URL}/api/mobiles/", timeout=5
            )
            if resp.status_code == 200:
                mobiles = resp.json()
                # Filter by query
                results["mobiles"] = [
                    m
                    for m in mobiles
                    if query.lower() in m.get("name", "").lower()
                    or query.lower() in m.get("brand", "").lower()
                    or query.lower() in m.get("description", "").lower()
                ]
        except Exception:
            pass

    return JsonResponse(results)
