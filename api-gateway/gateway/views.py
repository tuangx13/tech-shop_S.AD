import requests
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def verify_jwt_token(request):
    """Verify JWT token from request headers"""
    auth_header = request.headers.get("Authorization", "")

    if not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def proxy_request(target_url, request, extra_headers=None):
    """Proxy request to target service"""
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": request.headers.get("Authorization", ""),
        }
        if extra_headers:
            headers.update(extra_headers)

        if request.method == "GET":
            response = requests.get(target_url, headers=headers, params=request.GET)
        elif request.method == "POST":
            response = requests.post(
                target_url,
                headers=headers,
                json=json.loads(request.body) if request.body else {},
            )
        elif request.method == "PUT":
            response = requests.put(
                target_url,
                headers=headers,
                json=json.loads(request.body) if request.body else {},
            )
        elif request.method == "PATCH":
            response = requests.patch(
                target_url,
                headers=headers,
                json=json.loads(request.body) if request.body else {},
            )
        elif request.method == "DELETE":
            response = requests.delete(target_url, headers=headers)
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)

        # Handle empty response (204 No Content)
        if response.status_code == 204:
            return JsonResponse({"message": "Success"}, status=200)

        return JsonResponse(
            response.json() if response.content else {},
            status=response.status_code,
            safe=False,
        )

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=503)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON in request"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def auth_proxy(request, path=""):
    """Proxy to auth service - no token required"""
    target_url = f"{settings.AUTH_SERVICE_URL}/api/auth/{path}"
    return proxy_request(target_url, request)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def customer_proxy(request, path=""):
    """Proxy to customer service - requires customer token"""
    payload = verify_jwt_token(request)

    if payload is None:
        return JsonResponse({"error": "Invalid or expired token"}, status=401)

    if payload.get("role") != "customer":
        return JsonResponse({"error": "Customer access required"}, status=403)

    # Pass user_id to customer service
    extra_headers = {"X-User-Id": str(payload.get("user_id"))}
    target_url = f"{settings.CUSTOMER_SERVICE_URL}/api/customer/{path}"
    return proxy_request(target_url, request, extra_headers)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def staff_proxy(request, path=""):
    """Proxy to staff service - requires staff token"""
    payload = verify_jwt_token(request)

    if payload is None:
        return JsonResponse({"error": "Invalid or expired token"}, status=401)

    if payload.get("role") != "staff":
        return JsonResponse({"error": "Staff access required"}, status=403)

    # Pass user_id to staff service
    extra_headers = {"X-User-Id": str(payload.get("user_id"))}
    target_url = f"{settings.STAFF_SERVICE_URL}/api/staff/{path}"
    return proxy_request(target_url, request, extra_headers)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def laptop_proxy(request, path=""):
    """Proxy to laptop service - GET is public, write requires staff token"""
    if request.method == "GET":
        # Public read access
        target_url = f"{settings.LAPTOP_SERVICE_URL}/api/laptops/{path}"
        return proxy_request(target_url, request)
    else:
        # Write requires staff authentication
        payload = verify_jwt_token(request)
        if payload is None:
            return JsonResponse({"error": "Invalid or expired token"}, status=401)
        if payload.get("role") != "staff":
            return JsonResponse(
                {"error": "Staff access required for write operations"}, status=403
            )

        target_url = f"{settings.LAPTOP_SERVICE_URL}/api/laptops/{path}"
        return proxy_request(target_url, request)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def mobile_proxy(request, path=""):
    """Proxy to mobile service - GET is public, write requires staff token"""
    if request.method == "GET":
        # Public read access
        target_url = f"{settings.MOBILE_SERVICE_URL}/api/mobiles/{path}"
        return proxy_request(target_url, request)
    else:
        # Write requires staff authentication
        payload = verify_jwt_token(request)
        if payload is None:
            return JsonResponse({"error": "Invalid or expired token"}, status=401)
        if payload.get("role") != "staff":
            return JsonResponse(
                {"error": "Staff access required for write operations"}, status=403
            )

        target_url = f"{settings.MOBILE_SERVICE_URL}/api/mobiles/{path}"
        return proxy_request(target_url, request)


def health_check(request):
    """Health check endpoint"""
    return JsonResponse({"status": "healthy", "service": "api-gateway"})
