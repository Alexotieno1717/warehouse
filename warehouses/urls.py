from django.urls import path

from . import views

urlpatterns = [
    path('', views.warehouse_add, name='warehouse_add'),
    path('warehouse_list/', views.warehouse_list, name='warehouse_list'),
]
