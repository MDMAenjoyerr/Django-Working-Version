from blog.views import home , about , create
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home', home),
    path('about', about),
    path('create', create)
    
]
