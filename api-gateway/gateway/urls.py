from django.urls import path, re_path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    re_path(r'^api/auth/(?P<path>.*)$', views.auth_proxy, name='auth_proxy'),
    re_path(r'^api/customer/(?P<path>.*)$', views.customer_proxy, name='customer_proxy'),
    re_path(r'^api/staff/(?P<path>.*)$', views.staff_proxy, name='staff_proxy'),
    re_path(r'^api/laptops/(?P<path>.*)$', views.laptop_proxy, name='laptop_proxy'),
    re_path(r'^api/mobiles/(?P<path>.*)$', views.mobile_proxy, name='mobile_proxy'),
]
