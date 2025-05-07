from django.urls import path
from django.contrib import admin  # ✅ doğru olan bu
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]

