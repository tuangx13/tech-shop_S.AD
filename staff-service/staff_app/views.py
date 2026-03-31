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
from decimal import Decimal
from .forms import StaffRegistrationForm, LaptopForm, MobileForm


# ==================== TEMPLATE VIEWS ====================
def staff_login(request):
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
    return render(request, "staff_app/login.html")


def staff_register(request):
    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = StaffRegistrationForm()
    return render(request, "staff_app/register.html", {"form": form})


def staff_logout(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
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
        "laptops": laptops,
        "mobiles": mobiles,
        "total_laptops": len(laptops),
        "total_mobiles": len(mobiles),
    }
    return render(request, "staff_app/dashboard.html", context)


@login_required
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                data["price"] = str(data["price"])
                resp = requests.post(
                    f"{settings.LAPTOP_SERVICE_URL}/api/laptops/", json=data, timeout=5
                )
                if resp.status_code == 201:
                    messages.success(request, "Đã thêm laptop thành công!")
                    return redirect("dashboard")
                else:
                    messages.error(request, f"Lỗi: {resp.text}")
            except Exception as e:
                messages.error(request, f"Không thể kết nối đến Laptop Service: {e}")
    else:
        form = LaptopForm()
    return render(
        request,
        "staff_app/add_product.html",
        {"form": form, "product_type": "Laptop", "icon": "💻"},
    )


@login_required
def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                data["price"] = str(data["price"])
                resp = requests.post(
                    f"{settings.MOBILE_SERVICE_URL}/api/mobiles/", json=data, timeout=5
                )
                if resp.status_code == 201:
                    messages.success(request, "Đã thêm điện thoại thành công!")
                    return redirect("dashboard")
                else:
                    messages.error(request, f"Lỗi: {resp.text}")
            except Exception as e:
                messages.error(request, f"Không thể kết nối đến Mobile Service: {e}")
    else:
        form = MobileForm()
    return render(
        request,
        "staff_app/add_product.html",
        {"form": form, "product_type": "Điện thoại", "icon": "📱"},
    )


@login_required
def update_laptop(request, product_id):
    laptop_data = {}
    try:
        resp = requests.get(
            f"{settings.LAPTOP_SERVICE_URL}/api/laptops/{product_id}/", timeout=5
        )
        if resp.status_code == 200:
            laptop_data = resp.json()
    except Exception:
        messages.error(request, "Không thể lấy thông tin laptop.")
        return redirect("dashboard")

    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                data["price"] = str(data["price"])
                resp = requests.put(
                    f"{settings.LAPTOP_SERVICE_URL}/api/laptops/{product_id}/",
                    json=data,
                    timeout=5,
                )
                if resp.status_code == 200:
                    messages.success(request, "Đã cập nhật laptop thành công!")
                    return redirect("dashboard")
                else:
                    messages.error(request, f"Lỗi: {resp.text}")
            except Exception as e:
                messages.error(request, f"Lỗi kết nối: {e}")
    else:
        form = LaptopForm(initial=laptop_data)
    return render(
        request,
        "staff_app/update_product.html",
        {
            "form": form,
            "product_type": "Laptop",
            "icon": "💻",
            "product_id": product_id,
        },
    )


@login_required
def update_mobile(request, product_id):
    mobile_data = {}
    try:
        resp = requests.get(
            f"{settings.MOBILE_SERVICE_URL}/api/mobiles/{product_id}/", timeout=5
        )
        if resp.status_code == 200:
            mobile_data = resp.json()
    except Exception:
        messages.error(request, "Không thể lấy thông tin điện thoại.")
        return redirect("dashboard")

    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                data["price"] = str(data["price"])
                resp = requests.put(
                    f"{settings.MOBILE_SERVICE_URL}/api/mobiles/{product_id}/",
                    json=data,
                    timeout=5,
                )
                if resp.status_code == 200:
                    messages.success(request, "Đã cập nhật điện thoại thành công!")
                    return redirect("dashboard")
                else:
                    messages.error(request, f"Lỗi: {resp.text}")
            except Exception as e:
                messages.error(request, f"Lỗi kết nối: {e}")
    else:
        form = MobileForm(initial=mobile_data)
    return render(
        request,
        "staff_app/update_product.html",
        {
            "form": form,
            "product_type": "Điện thoại",
            "icon": "📱",
            "product_id": product_id,
        },
    )


# ==================== REST API VIEWS ====================
@csrf_exempt
@require_http_methods(["GET"])
def api_products(request):
    """Get all products from both services"""
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

    return JsonResponse(
        {
            "laptops": laptops,
            "mobiles": mobiles,
            "total_laptops": len(laptops),
            "total_mobiles": len(mobiles),
        }
    )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_laptops(request):
    """API for laptop management"""
    if request.method == "GET":
        try:
            resp = requests.get(
                f"{settings.LAPTOP_SERVICE_URL}/api/laptops/", timeout=5
            )
            return JsonResponse(
                resp.json() if resp.status_code == 200 else [], safe=False
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            if "price" in data and isinstance(data["price"], (int, float, Decimal)):
                data["price"] = str(data["price"])
            resp = requests.post(
                f"{settings.LAPTOP_SERVICE_URL}/api/laptops/", json=data, timeout=5
            )
            return JsonResponse(
                resp.json() if resp.content else {}, status=resp.status_code, safe=False
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def api_laptop_detail(request, product_id):
    """API for single laptop management"""
    url = f"{settings.LAPTOP_SERVICE_URL}/api/laptops/{product_id}/"

    if request.method == "GET":
        try:
            resp = requests.get(url, timeout=5)
            return JsonResponse(
                resp.json() if resp.status_code == 200 else {"error": "Not found"},
                status=resp.status_code,
                safe=False,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            if "price" in data and isinstance(data["price"], (int, float, Decimal)):
                data["price"] = str(data["price"])
            resp = requests.put(url, json=data, timeout=5)
            return JsonResponse(
                resp.json() if resp.content else {}, status=resp.status_code, safe=False
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "DELETE":
        try:
            resp = requests.delete(url, timeout=5)
            return JsonResponse(
                (
                    {"message": "Deleted successfully"}
                    if resp.status_code == 204
                    else resp.json() if resp.content else {}
                ),
                status=200 if resp.status_code == 204 else resp.status_code,
                safe=False,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_mobiles(request):
    """API for mobile management"""
    if request.method == "GET":
        try:
            resp = requests.get(
                f"{settings.MOBILE_SERVICE_URL}/api/mobiles/", timeout=5
            )
            return JsonResponse(
                resp.json() if resp.status_code == 200 else [], safe=False
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            if "price" in data and isinstance(data["price"], (int, float, Decimal)):
                data["price"] = str(data["price"])
            resp = requests.post(
                f"{settings.MOBILE_SERVICE_URL}/api/mobiles/", json=data, timeout=5
            )
            return JsonResponse(
                resp.json() if resp.content else {}, status=resp.status_code, safe=False
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def api_mobile_detail(request, product_id):
    """API for single mobile management"""
    url = f"{settings.MOBILE_SERVICE_URL}/api/mobiles/{product_id}/"

    if request.method == "GET":
        try:
            resp = requests.get(url, timeout=5)
            return JsonResponse(
                resp.json() if resp.status_code == 200 else {"error": "Not found"},
                status=resp.status_code,
                safe=False,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            if "price" in data and isinstance(data["price"], (int, float, Decimal)):
                data["price"] = str(data["price"])
            resp = requests.put(url, json=data, timeout=5)
            return JsonResponse(
                resp.json() if resp.content else {}, status=resp.status_code, safe=False
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)

    elif request.method == "DELETE":
        try:
            resp = requests.delete(url, timeout=5)
            return JsonResponse(
                (
                    {"message": "Deleted successfully"}
                    if resp.status_code == 204
                    else resp.json() if resp.content else {}
                ),
                status=200 if resp.status_code == 204 else resp.status_code,
                safe=False,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=503)
