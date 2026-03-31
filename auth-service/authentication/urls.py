from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('verify/', views.verify, name='verify'),
    path('me/', views.me, name='me'),
]
