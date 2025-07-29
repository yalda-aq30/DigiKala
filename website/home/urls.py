from django.contrib import admin
from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path('home/', views.home_response,name="home_response"),
    path('', views.home_view, name='home' ),
    path('base/', views.base_view, name='base')
]
