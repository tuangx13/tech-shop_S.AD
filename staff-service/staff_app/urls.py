from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path("", views.dashboard, name="home"),
    path("login/", views.staff_login, name="login"),
    path("register/", views.staff_register, name="register"),
    path("logout/", views.staff_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("laptop/add/", views.add_laptop, name="add_laptop"),
    path("mobile/add/", views.add_mobile, name="add_mobile"),
    path("laptop/update/<int:product_id>/", views.update_laptop, name="update_laptop"),
    path("mobile/update/<int:product_id>/", views.update_mobile, name="update_mobile"),
    # REST API endpoints
    path("api/staff/products/", views.api_products, name="api_products"),
    path("api/staff/laptops/", views.api_laptops, name="api_laptops"),
    path(
        "api/staff/laptops/<int:product_id>/",
        views.api_laptop_detail,
        name="api_laptop_detail",
    ),
    path("api/staff/mobiles/", views.api_mobiles, name="api_mobiles"),
    path(
        "api/staff/mobiles/<int:product_id>/",
        views.api_mobile_detail,
        name="api_mobile_detail",
    ),
]
