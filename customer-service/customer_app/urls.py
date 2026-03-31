from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path("", views.dashboard, name="home"),
    path("login/", views.customer_login, name="login"),
    path("register/", views.customer_register, name="register"),
    path("logout/", views.customer_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("search/", views.search_products, name="search"),
    path("cart/", views.view_cart, name="cart"),
    path("cart/add/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    # REST API endpoints
    path("api/customer/cart/", views.api_cart, name="api_cart"),
    path("api/customer/cart/<int:item_id>/", views.api_cart_item, name="api_cart_item"),
    path("api/customer/search/", views.api_search, name="api_search"),
]
