from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_add, name='product_add'),
    path('product_list/', views.product_list, name='product_list'),
]
