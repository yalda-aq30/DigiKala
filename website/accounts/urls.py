from django.contrib import admin
from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path('', views.account_view, name='accounts'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login')
]
